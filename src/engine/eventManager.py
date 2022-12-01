# -*- encoding: utf-8 -*-
import pygame
from time import time as getTime
from .events import *
from pyfirmata import util, STRING_DATA
from pymata4.pymata4 import Pymata4

class GameEvent():
    def __init__(self, type, data, time=0, repit=0):
        self.type = type
        self.data = data
        self.time = getTime()+time
        self._timeBase = time
        self.repit = repit

    def isFinished(self):
        return self.repit < 1

    def next(self):
        self.repit -= 1
        self.time += self._timeBase

    def __str__(self):
        data= dict(time=self.time, timeBase=self._timeBase, repit=self.repit, **self.data)
        return "GameEvent: {}".format(data)
    def __getattr__(self, name):
        return self.data[name]

class Button():
    def __init__(self, name, pin):
        self.name = name
        self.pin = pin
    
    def check(self, board):
        return not board.digital_read(self.pin)


class EventManager():
    def __init__(self, engine):
        self.engine = engine
        self.ScreenCharLimit = 16
        # conectamos a arduino:
        self._arduino = False
        try:
            self.board = Pymata4()
        except RuntimeError:
            engine.error("no se pudo conectar a arduino")
        else:
            self._arduino = True
            engine.log("arduino conectado exitosamente")
        # lista de botones, se tienen que conectar con el metodo: conectButtonArduino
        self.arduinoBtn = []
        self.events = [] # precondición: siempre estará ordenada de menor a mayor en tiempo
        self.audioExt = ".wav"

    def quit(self):
        pass

    def arduinoIsActive(self):
        return self._arduino

    def append(self, type, data, time, repit):
        """ agrega un evento a la lista de eventos pendientes. """
        event = GameEvent(type, data, time, repit)
        self.events.append(event)
        self.events.sort(key=lambda e: e.time)

    def clear(self):
        self.events.clear()

    def get(self):
        """ obtiene una lista de eventos a procesar. """
        time = getTime()
        ls = []
        for e in self.events:
            if e.time <= time:
                ls.append(e)
                e.next()
                if e.isFinished():
                    self.events.remove(e)
            else:
                break
        return ls

    def conectButtonArduino(self):
        """ realiza la activación de los botones preseteados en la configuración.
        precondición: verificar si está arduino activo antes de llamar a este método. """
        for key, btn in self.engine.config['buttons'].items():
            if isinstance(btn, int):
                self.board.set_pin_mode_digital_input_pullup(btn)
                self.arduinoBtn.append(Button(key, btn))
            else:
                if btn is not None:
                    self.engine.error("el pin {} no es válido para el botón {}.".format(btn, key))

    def message(self, name):
        path = pygame.mixer.Sound(self.engine._roottts+name+self.audioExt)
        try:
            return self.engine.voiceChannel.play(path)
        except FileNotFoundError:
            self.engine.error("No se encuentra el audio: '{}'".format(path))

    def display(self, text):
        text = str(text) # pasamos a str por si las dudas, por si recibimos en otro tipo.
        charLen = len(text)
        if charLen > self.ScreenCharLimit:
            # si son más del limite de caracteres lo acorta y arroja un error.
            self.engine.error(
                "se intentó enviar al display un texto de {} caracteres que supera el limite de {}.\n'{}'"
                .format(charLen, self.screenCharLimit, text))
            text = text[:self.screenCharLimit]
        if self.engine.modeDisplay and self._arduino:
            self.board._send_sysex(STRING_DATA, util.str_to_two_byte_iter(text))
        else:
            self.log("display: '{}'".format(text))

    def play(self, name, volume):
        path = self.engine._rootfx+name+self.audioExt
        try:
            sound = pygame.mixer.Sound(path)
        except FileNotFoundError:
            self.engine.error("No se encuentra el audio: '{}'".format(path))
        else:
            if volume:
                sound.set_volume(volume)
            return pygame.mixer.Sound.play(sound)

    def process(self, event):
        if event.type == pygame.KEYDOWN:
            self.engine.controller.keyDown(event.key)
            if event.key == pygame.K_ESCAPE:
                self.engine.finish()
        elif event.type == MESSAGE:
            self.message(event.path)
        elif event.type == AUDIO:
            self.play(event.name, event.volume)
        elif event.type == DISPLAY:
            self.display(event.text)
        elif event.type == CALLBACK:
            if event.args:
                event.callback(event.args)
            else:
                event.callback()
        elif event.type == GAME_Event:
            self.engine.controller.game(event)

    def checkArduino(self):
        if self._arduino:
            for btn in self.arduinoBtn:
                if btn.check(self.board):
                    self.engine.controller.buttonDown(btn.name)
