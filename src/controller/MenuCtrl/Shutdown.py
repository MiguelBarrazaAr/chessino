# -*- encoding: utf-8 -*-
from .MenuItem import MenuItem

class Shutdown(MenuItem):
    def start(self):
        self.audio = "apagar"
        self.engine.display('apagar')

    def back(self):
        pass

    def next(self):
        pass
