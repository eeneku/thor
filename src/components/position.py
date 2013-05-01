# -*- coding: utf-8 -*-

from engine import component

class Position(component.Component):
    """ Position component."""

    def __init__(self, *args, **kwargs):
        
        super(Position, self).__init__(*kwargs, **kwargs)
        
        self.x = 0
        self.y = 0
        