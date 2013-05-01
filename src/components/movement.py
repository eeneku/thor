# -*- coding: utf-8 -*-

from engine import component

class Movement(component.Component):
    """ Movement component."""

    def __init__(self, *args, **kwargs):
        
        super(Movement, self).__init__(*kwargs, **kwargs)
        
        self.x = 0
        self.y = 0
        self.direction = 0
        self.speed = 0