# -*- encoding: utf-8 -*-
from .MenuItem import MenuItem

class AjustW(MenuItem):
    def start(self):
        self.audio = "tiempo-blancas"
        self.engine.display('tiempo blancas')

    def back(self):
        pass

    def next(self):
        pass
