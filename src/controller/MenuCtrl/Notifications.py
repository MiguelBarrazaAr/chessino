# -*- encoding: utf-8 -*-
from .MenuItem import MenuItem

class Notifications(MenuItem):
    def start(self):
        self.audio = "aviso-tiempo"

    def back(self):
        pass

    def next(self):
        pass
