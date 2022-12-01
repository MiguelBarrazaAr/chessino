# -*- encoding: utf-8 -*-
from .MenuItem import MenuItem

class AjustB(MenuItem):
    def start(self):
        self.audio = "tiempo-negras"
        self.engine.display('tiempo negras')

    def back(self):
        pass

    def next(self):
        pass
