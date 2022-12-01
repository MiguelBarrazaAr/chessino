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
        # miramos que no esté bajada la bandera:
        if not self.engine.data['flag']:
            self.engine.data['pause'] = True
            self.engine.wait(0.1)
            self.error()
            self.engine.wait(1)
        else:
            if option:
                self.engine.clock.setActive(False)
                self.engine.message('reloj-pausado')
                self.engine.wait(1.3)
                self.engine.play("exit")
            else:
                self.engine.clock.setActive(True)
                self.engine.play("exit")
        self.engine.setController("Clock")

