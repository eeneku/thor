# -*- coding: utf-8 -*-

from engine import component

class TilemapRender(component.Component):
    """ Tilemap render component."""

    def __init__(self, *args, **kwargs):
        
        super(TilemapRender, self).__init__(*kwargs, **kwargs)
        
        self.world_x = 0
        self.world_y = 0
        
        self.view_x = 0
        self.view_y = 0
        self.view_width = 500
        self.view_height = 500
        
        self.width = 0
        self.height = 0