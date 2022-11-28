# -*- encoding: utf-8 -*-
import pygame
from time import time as getTime
from .events import *

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



class EventManager():
    def __init__(self, engine):
        self.engine = engine
        self.events = [] # precondición: siempre estará ordenada de menor a mayor en tiempo
        self.audioExt = ".wav"

    def quit(self):
        pass

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

    def message(self, name):
        path = pygame.mixer.Sound(self.engine._roottts+name+self.audioExt)
        try:
            return self.engine.voiceChannel.play(path)
        except FileNotFoundError:
            self.engine.error("No se encuentra el audio: '{}'".format(path))

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
        elif event.type == CALLBACK:
            if event.args:
                event.callback(event.args)
            else:
                event.callback()
        elif event.type == GAME_Event:
            self.engine.controller.game(event)
        