# -*- encoding: utf-8 -*-
from .Start import Start
from .Clock import Clock

def registerController(engine):
    engine.register(Clock)
    engine.register(Start)