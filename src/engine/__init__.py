# -*- encoding: utf-8 -*-
import sys
import pygame
import os
from time import time

from .events import *
from .eventManager import EventManager


class Engine():
    def __init__(self):
        self._controllers = {}
        self.controller = None
        self._active = True # indica si esta activo.
        # initialize:
        pygame.init()
        pygame.mixer.init()
        # reservamos un canal para los mensajes de voz
        self.voiceChannel = pygame.mixer.Channel(0)
        self.voiceChannel.set_volume(1.0)
        pygame.mixer.set_reserved(0)
        self.eventManager = EventManager(self)
        self.clock = None
        self.config = {}

    def register(self, controller):
        self._controllers[controller.__name__] = controller

    def loadConfig(self, config):
        self.config = config.__dict__
        
    def setTts(self, name):
        if os.path.exists('audios/'+name):
            self.ttsName = name
            self._roottts = "audios/"+self.ttsName+"/"
            self.log("se configuró como voz a: {}".format(name))
        else:
            raise ValueError('no se encuentra la carpeta de audios de la voz: '+name)

    
    def setController(self, name):
        try:
            self.controller = self._controllers[name](self)
        except KeyError:
            self.error("'{}' no es un controlador válido.".format(name))
        else:
            self.controller.start()
            self.log("controlador activo: {}".format(name))

    def appendEvent(self, typeEvent, data={}, repit=1):
        self.eventManager.append(typeEvent, data, self._time, repit)

    def error(self, text):
        self.log("error: "+text)

    def log(self, text):
        print(text)

    def run(self):
        # app config
        self.setTts(self.config['voice'])
        self._rootfx = "audios/fx/"
        self._rootmusic = "audios/music/"

        title = "{} ({})".format(self.config.get('title', ''), self.config.get('version', ''))
        self.log(title+" starting")
        # si inicia con windows mostramos ventana:
        if sys.platform.startswith('win'):
            width = self.config.get('width', 300)
            height = self.config.get('height', 200)
            self.screen = pygame.display.set_mode((width, height))
            pygame.display.set_caption(title)
            pygame.display.flip()


        """ ejecuta el loop game """
        try:
            # activamos la escucha de eventos:
            while self.isActive():
                self._time = 0 # reseteamos el contador de tiempo para eventos programados
                for event in (pygame.event.get() + self.eventManager.get()):
                    self.eventManager.process(event)
        except KeyboardInterrupt:
            self.finish()

    def isActive(self):
        return self._active

    def finish(self):
        self._active = False
        pygame.quit()
        self.eventManager.quit()
        print("finalizado")
        sys.exit()

    def wait(self, sec):
        self._time += sec

    def eventClear(self):
        self.eventManager.clear()

    def message(self, path):
        self.appendEvent(MESSAGE, {"path": path})

    def command(self, name, data=None, controller=None):
        self.appendEvent(COMMAND, {"name": name, "data": data, "controller": controller})

    def play(self, name, volume=None):
        self.appendEvent(AUDIO, {"name": name, "volume": volume})

    def callback(self, function, args=None):
        self.appendEvent(CALLBACK, {"callback": function, "args": args})

    def game(self, **data):
        self.appendEvent(GAME_Event, data)



def init():
    return Engine()