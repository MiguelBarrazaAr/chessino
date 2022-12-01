# -*- encoding: utf-8 -*-
from .ItemSwitch import ItemSwitch

class Increment(ItemSwitch):
    def start(self):
        self.audio = "incremento"
        self.setParam('add-increment')
        self.engine.display('incremento')
