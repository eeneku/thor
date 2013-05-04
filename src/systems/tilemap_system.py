# -*- coding: utf-8 -*-

from engine import system

from components import tilemap
from components import tileset

class TilemapSystem(system.System):
    """ Tilemap system. Handles tilemap stuff. """
    
    def __init__(self, entity_manager=None, *args, **kwargs):
        super(TilemapSystem, self).__init__(*args, **kwargs)
        
        self.entity_manager = entity_manager
    
    def update(self, dt):
        store = self.entity_manager.get_all_components_of_type(tilemap.Tilemap)
    
    
    