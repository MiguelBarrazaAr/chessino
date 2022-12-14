# -*- encoding: utf-8 -*-
class MenuItem():
    def __init__(self, engine):
        self.engine = engine
        self.audio = "name" # remplazar con el que corresponda
        self.id=0
        self.options = []
        self.label = ''
        self.start()
    
    def start(self):
        pass

    def back(self):
        self.move(-1)

    def next(self):
        self.move(1)

    def read(self):
        self.engine.message(self.audio)
        self.engine.display(self.label)

    def move(self, x):
        self.id = (self.id+x)%len(self.options)
        self.readOption(self.options[self.id])
    
    def readOption(self, option):
        pass

    def error(self):
        self.engine.play('error')
        self.engine.display('error')
