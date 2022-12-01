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
            # seteamos tiempos:
            if self.engine.data['white-turn']:
                value = self.setTimeByColor('white', s)
            else:
                value = self.setTimeByColor('black', s)
            self.alarm(value)
            self.showTime()

    def showTime(self):
        # mostramos tiempos|:
        self.engine.display("{} {}".format(self.formatTime('white'), self.formatTime('black')))

    def setTimeByColor(self, color, seconds):
        value = self.engine.data[color]-seconds
        if value <= 0:
            value=0
            self.finish()
        self.engine.data[color] = value
        return value

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
        # bajamos bandera y pausamos:
        self.engine.data["flag"] = False
        self.engine.data["pause"] = True
        # alerta de sonido:
        self.engine.play('finish')
        self.engine.wait(1.5)
        if self.engine.data["white-turn"]:
            self.engine.display("gana negras")
            self.engine.message('blancas')
        else:
            self.engine.display("gana blancas")
            self.engine.message('negras')
        self.engine.wait(1)
        self.engine.message('no-tiempo')
        self.engine.wait(2)
        self.engine.play('finish')

    def setPreset(self, preset):
        secs = self.toSeconds(preset['hour'], preset['minute'], preset['second'])
        # lo seteamos como default
        self.engine.data['time-default'] = secs
        self.engine.data['increment-default'] = preset['increment']

    def setTime(self):
        """ seteamos tiempo default a cada jugador """
        secs = self.engine.data['time-default']
        self.engine.data['white'] = secs
        self.engine.data['black'] = secs
        inc = self.engine.data['increment-default']
        self.engine.data['increment'] = inc
        self.engine.data['flag'] = True
        self.engine.data['pause'] = True
        self.engine.data['add-increment'] = inc>0

    def toSeconds(self, hour, minute, second):
        return hour*3600 + minute*60 + second
