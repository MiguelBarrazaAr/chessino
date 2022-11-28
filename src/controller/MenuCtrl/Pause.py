# -*- encoding: utf-8 -*-
from .MenuItem import MenuItem

class Pause(MenuItem):
    def start(self):
        self.audio = "pausar"

    def back(self):
        pass

    def next(self):
        pass
