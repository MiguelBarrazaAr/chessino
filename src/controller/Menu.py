# -*- encoding: utf-8 -*-
from .Controller import Controller

class Menu(Controller):
    def start(self):
        self.play("menu")
        self.readMenu()

    def b1(self):
        print("negras")

    def b2(self):
        print("lee negras")

    def w1(self):
        print("blancas")

    def w2(self):
        print("lee blancas")

    def menu(self):
        self.play("exit")
        self.setController("Clock")

    def readMenu(self):
        pass