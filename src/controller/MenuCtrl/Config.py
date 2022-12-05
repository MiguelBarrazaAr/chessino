# -*- encoding: utf-8 -*-
from .MenuItem import MenuItem

class Config(MenuItem):
    def start(self):
        self.label = 'config tiempo'
        self.audio = "configurar-tiempos"

    def back(self):
        self.active()

    def next(self):
        self.active()
    
    def active(self):
        self.engine.wait(0.1)
        self.engine.callback(self.engine.setController, 'ConfigTimeMenu')
