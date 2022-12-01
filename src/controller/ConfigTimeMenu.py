# -*- encoding: utf-8 -*-
from .Controller import Controller
from .MenuCtrl import *

class ConfigTimeMenu(Controller):
    def start(self):
        self.options = ["horas", "minutos", "segundos", "incremento", "guardar-cambios"]
        self.id=0
        self.wait(0.2)
        self.callback(self.readMenu)

    def b1(self):
        self.move(-1)

    def move(self, x):
        self.eventClear()
        self.id = (self.id+x)%len(self.options)
        if self.engine.data['sounds']:
            self.play("move")
            self.wait(0.1)
        self.callback(self.readMenu)

    def b2(self):
        if self.engine.data['sounds']:
            self.play('item')
            self.wait(0.1)
        self.getOption().back()

    def w1(self):
        self.move(1)

    def w2(self):
        option = self.getOption()
        if self.engine.data['sounds']:
            self.play('item')
            self.wait(0.1)
        if option == "guardar-cambios":
            pass #self.save()
        elif option == "incremento":
            self.engine.data['increment-default']+=1
            self.readMenu()
        elif option == "horas":
            self.engine.data['time-default']+=3600
            self.readMenu()
        

    def menu(self):
        self.play("exit")
        self.setController("Clock")

    def getOption(self):
        return self.options[self.id]

    def readMenu(self):
        option = self.getOption()
        if option == "guardar-cambios":
            self.speak(option)
        elif option == "incremento":
            self.speak(option)
            self.wait(0.8)
            inc = self.engine.data['increment-default']
            self.engine.clockTts.readTime(inc)
        elif option == "horas":
            time = (self.engine.data['time-default']//3600)*3600
            if time == 0:
                self.speak('horas')
            
            self.engine.clockTts.readTime(time)
        elif option == "minutos":
            time = ((self.engine.data['time-default']%3600)//60)*60
            if time == 0:
                self.speak('minutos')
            self.engine.clockTts.readTime(time)
        elif option == "segundos":
            time = self.engine.data['time-default']%60
            if time == 0:
                self.speak('segundos')
            self.engine.clockTts.readTime(time)