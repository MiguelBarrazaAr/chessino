# -*- encoding: utf-8 -*-
import pygame

id = 33000

def custom_id():
    global id
    id+=1
    return id-1


custom_type = getattr(pygame.event, "custom_type", custom_id)


AUDIO = custom_type()
MESSAGE = custom_type()
MESSAGE_Stop = custom_type()
CALLBACK = custom_type()
CONTROLLER = custom_type()
COMMAND = custom_type()
GAME_Event = custom_type()
