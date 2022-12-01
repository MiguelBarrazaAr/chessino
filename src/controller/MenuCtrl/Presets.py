# -*- encoding: utf-8 -*-
from .MenuItem import MenuItem

class Presets(MenuItem):
    def start(self):
        self.audio = "presets"
        self.engine.display('presets')

    def back(self):
        pass

    def next(self):
        pass
