# -*- encoding: utf-8 -*-
from .Start import Start
from .Clock import Clock
from .Menu import Menu
from .ConfigTimeMenu import ConfigTimeMenu

def registerController(engine):
    engine.register(Clock)
    engine.register(Menu)
    engine.register(Start)
    engine.register(ConfigTimeMenu)
    