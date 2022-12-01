# -*- encoding: utf-8 -*-
import engine
from model.Clock import Clock
from model.ClockTts import ClockTts
import config
from src.controller import registerController

engine = engine.init()
registerController(engine)
engine.loadConfig(config)
engine.loadUserData()
engine.clock = Clock(engine)
engine.clockTts = ClockTts(engine)
engine.setController("Start")
engine.run()
