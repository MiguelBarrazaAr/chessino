# -*- encoding: utf-8 -*-
from .Controller import Controller

class Clock(Controller):
    def start(self):
        if not self.engine.data['pause']:
            self.engine.clock.setActive(True)

    def b1(self):
        print("negras")

    def b2(self):
        self.engine.eventClear()
        if self.engine.data['sounds']:
            self.engine.play('item')
            self.engine.wait(0.1)
        if self.engine.data['pause']:
            self.engine.clockTts.readOnlyBlackTime()
        else:
            if not self.engine.data['white-turn']:
                self.engine.clockTts.readBlackTime()
            else:
                self.engine.play('error')

    def w1(self):
        print("blancas")

    def w2(self):
        self.engine.eventClear()
        if self.engine.data['sounds']:
            self.engine.play('item')
            self.engine.wait(0.1)
        if self.engine.data['pause']:
            self.engine.clockTts.readOnlyWhiteTime()
        else:
            if self.engine.data['white-turn']:
                self.engine.clockTts.readWhiteTime()
            else:
                self.engine.play('error')

    def menu(self):
        self.engine.eventClear()
        self.setController("Menu")