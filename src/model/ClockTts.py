# -*- encoding: utf-8 -*-

class ClockTts():
    def __init__(self, engine):
        self.engine = engine
        self.play = engine.play
        self.wait = engine.wait
        self.speak = engine.message

    def readOnlyWhiteTime(self):
        self.readTime('white')

    def readWhiteTime(self):
        pass

    def readOnlyBlackTime(self):
        self.readTime('black')

    def readTime(self, color):
        time = self.getTimeOf(color)
        if color == 'white':
            self.engine.message('blancas')
        else:
            self.engine.message('negras')
        h, m, s = time
        if h > 0:
            self.wait(0.9)
            self.engine.message('number/'+str(h))
            self.wait(1)
            if h > 1:
                self.engine.message('horas')
            else:
                self.engine.message('hora')
        if m > 0:
            self.wait(0.9)
            self.engine.message('number/'+str(m))
            self.wait(1)
            if m > 1:
                self.engine.message('minutos')
            else:
                self.engine.message('minuto')
        if s > 0:
            self.wait(0.9)
            self.engine.message('number/'+str(s))
            self.wait(1)
            if s > 1:
                self.engine.message('segundos')
            else:
                self.engine.message('segundo')

    def readBlackTime(self):
        pass

    def getTimeOf(self, color):
        t = self.engine.data[color]
        ms = t//60
        s = t%60
        h = ms//60
        m = ms%60
        return (h, m, s)