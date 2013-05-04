# -*- coding: utf-8 -*-

from engine import system

from components import tilemap
from components import tileset

class TilemapRenderSystem(system.System):
    """ Tilemap render system. Draws tiles. """
    
    def __init__(self, entity_manager=None, *args, **kwargs):
        super(TilemapRenderSystem, self).__init__(*args, **kwargs)
        
        self.entity_manager = entity_manager
    
    def on_draw(self):
        store = self.entity_manager.get_all_components_of_type(tilemap.Tilemap)

        if store:
            for entity, component in store.iteritems():
                tset = self.entity_manager.get_component(entity, tileset.Tileset)
                
                if tset:
                    try:
                        tilesize = tset.tiles[0].width
                        blit_y = component.y
                        tilecounter = 0
                        
                        for y in range(0, component.height):
                            blit_x = component.x
                            
                            for x in range(0, component.width):
                                tset.tiles[component.tiles[tilecounter]].blit(blit_x, blit_y)
                                
                                blit_x = blit_x + tilesize
                            blit_y = blit_y + tilesize
                            
                    except IndexError:
                        print("Oops! Tile not found.")
