# -*- encoding: utf-8 -*-
from .Dialog import Dialog

class Start(Dialog):
    def start(self):
        self.play("on")
        self.wait(1)
        self.play("chessino")
        self.wait(1.3)
        self.play("none")
        self.wait(1)
        self.speak("listo")
        self.callback(self.setController, "Clock")
