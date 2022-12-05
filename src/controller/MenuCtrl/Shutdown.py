# -*- encoding: utf-8 -*-
from .MenuItem import MenuItem
import os

class Shutdown(MenuItem):
    def start(self):
        self.audio = "apagar"
        self.label = 'apagar'

    def back(self):
        self.shutdownActive()

    def next(self):
        self.shutdownActive()

    def shutdownActive(self):
        self.engine.wait(0.1)
        self.engine.play('off')
        self.engine.wait(0.8)
        self.shutdownNow()

    def shutdownNow(self):
        os.system("shutdown /s /t 1") 