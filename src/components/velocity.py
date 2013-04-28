# -*- coding: utf-8 -*-

from engine import component

class Velocity(component.Component):
    """ Velocity component."""

    def __init__(self, *args, **kwargs):
        
        super(Velocity, self).__init__(*kwargs, **kwargs)
        
        self.x = 0
        self.y = 0