# -*- encoding: utf-8 -*-
from .MenuItem import MenuItem

class Shutdown(MenuItem):
    def start(self):
        self.audio = "apagar"

    def back(self):
        pass

    def next(self):
        pass