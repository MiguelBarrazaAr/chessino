# -*- encoding: utf-8 -*-
from .ItemSwitch import ItemSwitch

class Alarms(ItemSwitch):
    def start(self):
        self.audio = "alarmas"
        self.setParam('alarms')
        self.label = 'alarmas'
