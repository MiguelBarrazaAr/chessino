# -*- encoding: utf-8 -*-
from .MenuItem import MenuItem

class ItemSwitch(MenuItem):
    def setParam(self, param):
        self.param = param

    def move(self, x):
        option = not self.engine.data[self.param]
        self.engine.data[self.param] = option 
        self.readOption(option)

    def readOption(self, option):
        if option:
            self.engine.message('activado')
        else:
            self.engine.message('desactivado')
