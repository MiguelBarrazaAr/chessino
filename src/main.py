# -*- encoding: utf-8 -*-
import engine
from controller import registerController
import config 

engine = engine.init()
registerController(engine)
engine.loadConfig(config)
engine.setController("Start")
engine.run()
