# -*- encoding: utf-8 -*-

class Clock():
    def __init__(self, engine):
        self.engine = engine
        self.active = False

    def setActive(self, status):
        self.active = status
        if status:
            self.engine.log("Reloj activo")
        else:
            self.engine.log("Reloj pausado")

    def tick(self):
        pass
        