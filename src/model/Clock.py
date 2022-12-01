# -*- encoding: utf-8 -*-
from time import time

class Clock():
    def __init__(self, engine):
        self.engine = engine
        self.active = False
        self.time = 0 # tiempo de la activación.
        self.alarmsList = self.engine.data["alarm-list"]

    def setActive(self, status):
        self.active = status
        if status:
            self.engine.log("Reloj activo")
            self.time = self.getTime()
        else:
            self.engine.log("Reloj pausado")
            self.time=0

    def getTime(self):
        return int(time())

    def tick(self):
        current = self.getTime()
        if self.active and self.time < current:
            s = current - self.time
            self.time = current
            if self.engine.data['white-turn']:
                value = self.engine.data['white']-s
                self.engine.data['white'] = value
            else:
                value = self.engine.data['black']-s
                self.engine.data['black'] = value
            # todo: agregar validaciones para que nunca el tiempo sea valores negativos.
            if value == 0:
                self.finish()
            else:
                self.alarm(value)
            # mostramos valor:
            self.engine.display("{} {}".format(self.formatTime('white'), self.formatTime('black')))

    def formatTime(self, color):
        t = self.engine.data[color]
        m = t//60
        s=t%60
        return "{}:{}".format(m,s)

    def alarm(self, value):
        if value in self.alarmsList:
            self.engine.clockTts.alert(value)

    def finish(self):
        self.setActive(False)
        self.engine.data["flag"] = False
        if self.engine.data["white-turn"]:
            self.engine.display("gana negras")
        else:
            self.engine.display("gana blancas")
        self.engine.play('finish')
        self.engine.wait(1)
        self.engine.play('finish')