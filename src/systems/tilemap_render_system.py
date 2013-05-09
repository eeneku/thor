# -*- coding: utf-8 -*-

import math
from engine import system

from components import tilemap
from components import tilemap_render

class TilemapRenderSystem(system.System):
    """ Tilemap render system. """
    
    def __init__(self, entity_manager=None, *args, **kwargs):
        super(TilemapRenderSystem, self).__init__(*args, **kwargs)
        
        self.entity_manager = entity_manager
    
    def update(self, dt):
        store = self.entity_manager.get_all_components_of_type(tilemap.Tilemap)

        if store:
            for entity, component in store.iteritems():
                trender = self.entity_manager.get_component(entity, tilemap_render.TilemapRender)
                
                if trender and trender.need_to_update:
                    tiles_to_draw = ((int(math.floor(trender.world_y/component.tileheight)), int((trender.world_y+trender.view_height)/component.tileheight + 2)),
                                     (int(math.floor(trender.world_x/component.tilewidth)), int((trender.world_x+trender.view_width)/component.tilewidth + 2)))
                    
                    #print(math.floor(trender.world_y/component.tileheight), tiles_to_draw)
                        
                    view_y = trender.view_y - component.tileheight + trender.world_y % component.tileheight
                    
                    visible_tiles = []
                
                    for y in range(tiles_to_draw[0][0], tiles_to_draw[0][1]):
                        view_x = trender.view_x - trender.world_x % component.tilewidth
                        
                        for x in range(tiles_to_draw[1][0], tiles_to_draw[1][1]):
                            for layer in reversed(component.layers):
                                if (x,y) in layer.tiles:
                                    layer.tiles[(x,y)].visible = True

                                    visible_tiles.append(layer.tiles[(x,y)])


                                view_x = view_x + component.tilewidth
                                
                        view_y = view_y - component.tileheight
                        
                    new_visible_set = set(visible_tiles)

                    sprites_over_view = trender.visible_tiles.difference(new_visible_set)
                    trender.visible_tiles = new_visible_set
  
                    for sprite in sprites_over_view:
                        sprite.visible = False
                        sprite.batch = None
                        
                    trender.need_to_update = False
                    
