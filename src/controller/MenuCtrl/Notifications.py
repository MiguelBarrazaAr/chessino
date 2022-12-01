# -*- encoding: utf-8 -*-
from .ItemSwitch import ItemSwitch

class Notifications(ItemSwitch):
    def start(self):
        self.audio = "aviso-tiempo"
        self.setParam('notifications')
        self.label = 'notificacion'
