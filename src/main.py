# -*- encoding: utf-8 -*-
import engine
from controller import registerController
from model.Clock import Clock
from model.ClockTts import ClockTts
import config 

engine = engine.init()
registerController(engine)
engine.loadConfig(config)
engine.loadUserData()
engine.clock = Clock(engine)
engine.clockTts = ClockTts(engine)
engine.setController("Start")
engine.run()
