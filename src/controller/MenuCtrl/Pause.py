# -*- encoding: utf-8 -*-
from .ItemSwitch import ItemSwitch

class Pause(ItemSwitch):
    def start(self):
        self.audio = "pausar"
        self.setParam('pause')

    def read(self):
        if self.engine.data['pause']:
            self.engine.message('continuar')
            self.engine.display('continuar')
        else:
            self.engine.message('pausar')
            self.engine.display('pausar')

    def readOption(self, option):
        if option:
            self.engine.clock.setActive(False)
            self.engine.message('reloj-pausado')
            self.engine.wait(1.3)
        else:
            self.engine.clock.setActive(True)
        self.engine.play("exit")
        self.engine.setController("Clock")

