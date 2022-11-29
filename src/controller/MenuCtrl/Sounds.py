# -*- encoding: utf-8 -*-
from .ItemSwitch import ItemSwitch

class Sounds(ItemSwitch):
    def start(self):
        self.audio = "sonidos"
        self.setParam('sounds')
