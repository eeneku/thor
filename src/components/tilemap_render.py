# -*- coding: utf-8 -*-

from engine import component

class TilemapRender(component.Component):
    """ Tilemap render component."""

    def __init__(self, *args, **kwargs):
        
        super(TilemapRender, self).__init__(*kwargs, **kwargs)
        
        self.world_x = 0
        self.world_y = 0
        self.need_to_update = True
        
        self.view_x = 0
        self.view_y = 720
        self.view_width = 1280
        self.view_height = 720
        
        self.visible_tiles = set()