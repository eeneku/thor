# -*- coding: utf-8 -*-

from engine import component

class PlayerInput(component.Component):
    """ Player input component."""

    def __init__(self, *args, **kwargs):
        
        super(PlayerInput, self).__init__(*kwargs, **kwargs)
        
        self.move_left = None
        self.move_right = None
        self.move_up = None
        self.move_left = None
        