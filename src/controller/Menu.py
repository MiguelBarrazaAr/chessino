# -*- encoding: utf-8 -*-
from .Controller import Controller

class Menu(Controller):
    def start(self):
        self.options = ["config", "increment", "ajust-w", "ajust-b", "reset", "sounds", "alarts", "notifications", "voices", "presets", "shutdown", "pause"]
        self.id=0
        self.play("menu")
        self.wait(0.5)
        self.callback(self.readMenu)

    def b1(self):
        self.mover(-1)

    def mover(self, x):
        self.eventClear()
        self.move(x)
        self.play("move")
        self.wait(0.1)
        self.callback(self.readMenu)

    def b2(self):
        print("lee negras")

    def w1(self):
        self.mover(1)

    def w2(self):
        print("lee blancas")

    def menu(self):
        self.play("exit")
        self.setController("Clock")

    def move(self, x):
        self.id = (self.id+x)%len(self.options)
    
    def getOption(self):
        return self.options[self.id]

    def readMenu(self):
        option = self.getOption()
        if option == "config":
            self.speak("configurar-tiempos")
        elif option == "increment":
            self.speak("incremento")
        elif option == "ajust-w":
            self.speak("tiempo-blancas")
        elif option == "ajust-b":
            self.speak("tiempo-negras")
        elif option == "reset":
            self.speak("reiniciar-tiempos")
        elif option == "sounds":
            self.speak("sonidos")
        elif option == "alarts":
            self.speak("alarmas")
        elif option == "notifications":
            self.speak("aviso-tiempo")
        elif option == "voices":
            self.speak("voz")
        elif option == "presets":
            self.speak("presets")
        elif option == "shutdown":
            self.speak("apagar")
        elif option == "pause":
            self.speak("pausar")