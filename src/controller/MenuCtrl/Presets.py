# -*- encoding: utf-8 -*-
from .MenuItem import MenuItem

class Presets(MenuItem):
    def start(self):
        self.audio = "presets"
        self.label = 'presets'
        self.id=0
        self.max=5

    def move(self, x):
        self.id=(self.id+x)%self.max
        path = 'presets/'+str(self.id)+'/'
        self.engine.play(path+'audio')
        p=self.engine.loadPreset('audios/fx/'+path+'config.json')
        self.engine.display(p['display'])