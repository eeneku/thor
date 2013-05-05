# -*- coding: utf-8 -*-

from engine import component

class Tileset(component.Component):
    """ Tileset component."""

    def __init__(self, *args, **kwargs):
        
        super(Tileset, self).__init__(*kwargs, **kwargs)
        
        self.tiles = []
        self.images = []
        