# -*- encoding: utf-8 -*-
from .MenuItem import MenuItem

class Voices(MenuItem):
    def start(self):
        self.audio = "voz"
        self.id = self.engine.config['voices'].index(self.engine.config['voice'])
        self.options = self.engine.config['voices']
        self.label = 'voz'

    def readOption(self, option):
        self.engine.setTts(option)
        self.engine.message('name')
        self.engine.display('voz '+option)
