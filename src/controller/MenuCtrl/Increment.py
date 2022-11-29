# -*- encoding: utf-8 -*-
from .ItemSwitch import ItemSwitch

class Sounds(ItemSwitch):
    def Increment(self):
        self.audio = "incremento"
        self.setParam('add-increment')
