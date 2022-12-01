# -*- encoding: utf-8 -*-
KeysMethod= {
    "menu": "menu",
    "white": "w1",
    "whiteRead": "w2",
    "black": "b1",
    "blackRead": "b2",
}



class Controller():
    def __init__(self, engine):
        self.engine = engine
        self.play = engine.play
        self.wait = engine.wait
        self.speak = engine.message
        self.callback = engine.callback
        self.eventClear = engine.eventClear
        self.setController = engine.setController
        self.display = self.engine.display
        self.init()

    def init(self):
        pass

    def start(self):
        pass

    def enter(self):
        pass

    def w1(self):
        pass

    def w2(self):
        pass

    def b1(self):
        pass

    def b2(self):
        pass

    def menu(self):
        pass

    def keyDown(self, keyId):
        values = list(self.engine.config['keys'].values())
        try:
            pos = values.index(keyId)
        except ValueError:
            pass
        else:
            funcName = list(self.engine.config['keys'].keys())[pos]
            getattr(self, KeysMethod.get(funcName))()

    def buttonDown(self, name):
        try:
            funcName = KeysMethod[name]
        except KeyError:
            pass
        else:
            getattr(self, funcName)()

    def game(self, event):
        pass

    def error(self):
        self.play('error')
        self.engine.display('error')
