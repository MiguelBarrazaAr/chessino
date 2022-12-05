# -*- encoding: utf-8 -*-
import os
# Print the current working directory
print("Current working directory: {0}".format(os.getcwd()))

# Change the current working directory
os.chdir('/home/miguel/chessino/src')

import engine
from model.Clock import Clock
from model.ClockTts import ClockTts
import config
from controller import registerController

engine = engine.init()
registerController(engine)
engine.loadConfig(config)
engine.loadUserData()
engine.clock = Clock(engine)
engine.clockTts = ClockTts(engine)
engine.setController("Start")
engine.run()
