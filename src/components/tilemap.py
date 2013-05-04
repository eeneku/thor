# -*- coding: utf-8 -*-

from engine import component

class Tilemap(component.Component):
    """ Tilemap component."""

    def __init__(self, *args, **kwargs):
        
        super(Tilemap, self).__init__(*kwargs, **kwargs)
        
        self.tiles = []
        
        self.world_x = 0
        self.world_y = 0
        
        self.x = 0
        self.y = 0
        
        self.width = 0
        self.height = 0