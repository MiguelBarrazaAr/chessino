# -*- encoding: utf-8 -*-
from .MenuItem import MenuItem

class Alarms(MenuItem):
    def start(self):
        self.audio = "alarmas"

    def back(self):
        pass

    def next(self):
        pass
