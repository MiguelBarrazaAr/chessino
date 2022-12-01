# -*- encoding: utf-8 -*-
from .Controller import Controller

class Clock(Controller):
    def start(self):
        if not self.engine.data['pause']:
            self.engine.clock.setActive(True)

    def b1(self):
        self.engine.eventClear()
        if self.engine.data['flag'] and not self.engine.data['pause'] and not self.engine.data['white-turn']:
            self.engine.data['white-turn'] = True
            # agregamos incremento:
            if self.engine.data['add-increment']:
                self.engine.data['black'] = self.engine.data['black'] + self.engine.data['increment']
            # reproducimos aviso:
            self.engine.play('on')
            self.engine.wait(0.6)
            self.engine.message('turno')
            self.engine.wait(1)
            self.engine.message('blancas')
        else:
            self.error()

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
                self.error()

    def w1(self):
        self.engine.eventClear()
        if self.engine.data['flag'] and not self.engine.data['pause'] and self.engine.data['white-turn']:
            self.engine.data['white-turn'] = False
            # agregamos incremento:
            if self.engine.data['add-increment']:
                self.engine.data['white'] = self.engine.data['white'] + self.engine.data['increment']
            # reproducimos aviso:
            self.engine.play('on')
            self.engine.wait(0.6)
            self.engine.message('turno')
            self.engine.wait(1)
            self.engine.message('negras')
        else:
            self.error()

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
                self.error()

    def menu(self):
        self.engine.eventClear()
        self.setController("Menu")