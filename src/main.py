# -*- encoding: utf-8 -*-
import engine
from controller.start import Start
import config 

engine = engine.init()
engine.loadConfig(config)
engine.setController(Start)
engine.run()
