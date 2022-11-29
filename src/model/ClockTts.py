# -*- encoding: utf-8 -*-

class ClockTts():
    def __init__(self, engine):
        self.engine = engine
        self.play = engine.play
        self.wait = engine.wait
        self.speak = engine.message

    def readOnlyWhiteTime(self):
        pass

    def readWhiteTime(self):
        pass

    def readOnlyBlackTime(self):
        pass

    def readBlackTime(self):
        pass
