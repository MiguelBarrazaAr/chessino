# -*- encoding: utf-8 -*-
from .MenuItem import MenuItem

class Increment(MenuItem):
    def start(self):
        self.audio = "incremento"

    def back(self):
        pass

    def next(self):
        pass
