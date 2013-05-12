# -*- coding: utf-8 -*-

from engine import component

class Tilemap(component.Component):
    """ Tilemap component."""

    def __init__(self, *args, **kwargs):
        
        super(Tilemap, self).__init__(*kwargs, **kwargs)
        
        self.layers = []
        self.tileset_bin = None
        
        self.tilewidth = 0
        self.tileheight = 0
        
        self.width = 0
        self.height = 0
        
        self.version = ""
        