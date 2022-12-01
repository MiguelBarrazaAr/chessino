# -*- encoding: utf-8 -*-
from .MenuItem import MenuItem

class Reset(MenuItem):
    def start(self):
        self.audio = "reiniciar-tiempos"
        self.label = 'reiniciar tiemp'

    def back(self):
        self.setTime()

    def next(self):
        self.setTime()

    def setTime(self):
        self.engine.clock.setTime()
        self.engine.wait(0.2)
        self.engine.message('reiniciar-aviso')
        self.engine.wait(1.5)
        self.engine.clockTts.readTime(self.engine.data['time-default'])
        self.engine.wait(1)
        self.engine.controller.menu()
