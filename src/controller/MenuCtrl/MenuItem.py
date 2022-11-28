# -*- encoding: utf-8 -*-
class MenuItem():
    def __init__(self, engine):
        self.engine = engine
        self.audio = "name" # remplazar con el que corresponda
        self.start()
    
    def start(self):
        pass

    def back(self):
        pass

    def next(self):
        pass

    def read(self):
        self.engine.message(self.audio)