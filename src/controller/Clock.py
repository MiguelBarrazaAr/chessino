# -*- encoding: utf-8 -*-
from .Controller import Controller

class Clock(Controller):
    def start(self):
        if not self.engine.data['pause']:
            self.engine.clock.setActive(True)

    def b1(self):
        print("negras")

    def b2(self):
        self.engine.clockTts.readOnlyBlackTime()

    def w1(self):
        print("blancas")

    def w2(self):
        self.engine.clockTts.readOnlyWhiteTime()

    def menu(self):
        self.setController("Menu")