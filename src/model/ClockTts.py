# -*- encoding: utf-8 -*-

class ClockTts():
    def __init__(self, engine):
        self.engine = engine
        self.play = engine.play
        self.wait = engine.wait
        self.speak = engine.message

    def readOnlyWhiteTime(self):
        self.readTimeByColor('white')

    def readWhiteTime(self):
        self.readOnlyWhiteTime()
        self.wait(1.3)
        self.readOnlyBlackTime()

    def readOnlyBlackTime(self):
        self.readTimeByColor('black')

    def readTimeByColor(self, color):
        if color == 'white':
            self.engine.message('blancas')
        else:
            self.engine.message('negras')
        self.readTime(self.engine.data[color])

    def readTime(self, time):
        h, m, s = self.unpackTime(time)
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
        self.readOnlyBlackTime()
        self.wait(1.3)
        self.readOnlyWhiteTime()

    def unpackTime(self, time):
        ms = time//60
        s = time%60
        h = ms//60
        m = ms%60
        return (h, m, s)

    def alert(self, time):
        """ notifica un alerta """
        self.engine.play('alert')
        self.engine.wait(0.1)
        self.readTime(time)
            