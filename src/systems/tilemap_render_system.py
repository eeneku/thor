# -*- coding: utf-8 -*-

import pyglet
import math
from engine import system

from components import tilemap
from components import tilemap_render

class TilemapRenderSystem(system.System):
    """ Tilemap render system. """
    
    def __init__(self, entity_manager=None, *args, **kwargs):
        super(TilemapRenderSystem, self).__init__(*args, **kwargs)
        
        self.entity_manager = entity_manager
        
    def on_draw(self):
        store = self.entity_manager.get_all_components_of_type(tilemap_render.TilemapRender)

        if store:  
            for entity, component in store.iteritems():      
                component.batch.draw()
    
    def update(self, dt):
        """ This method is supposed to narrow tiles to draw to the tiles visible on the screen. """
        store = self.entity_manager.get_all_components_of_type(tilemap.Tilemap)

        if store:
            for entity, component in store.iteritems():
                trender = self.entity_manager.get_component(entity, tilemap_render.TilemapRender)
                
                if trender and trender.need_to_update:
                    """ Lets calculate the tiles. """
                    tiles_to_draw = ((int(math.floor(trender.world_y/component.tileheight)), int((trender.world_y+trender.view_height)/component.tileheight + 2)),
                                     (int(math.floor(-trender.world_x/component.tilewidth)), int((-trender.world_x+trender.view_width)/component.tilewidth + 2)))

                    vertex_data = []
                    texture_data = []
                    color_data = []
                    vertices = 0

                    for y in range(tiles_to_draw[0][0], tiles_to_draw[0][1]):
                        # 720 is screen height!
                        y1 = (720 - trender.view_y) + component.tileheight * -y
                        y2 = y1 - component.tileheight
                        
                        for x in range(tiles_to_draw[1][0], tiles_to_draw[1][1]):
                            x1 = trender.view_x + component.tilewidth * x
                            x2 = x1 + component.tilewidth
                
                            
                            for layer in reversed(component.layers):
                                if (x,y) in layer.tiles:
                                    
                                    vertex_data.extend([x1, y2, x2, y2, x2, y1, x1, y1])
                                    texture_data.extend(component.tileset_bin.tiles[layer.tiles[(x,y)].gid].tex_coords)
                                    color_data.extend((255, 255, 255, 255)*4)
                   
                                    vertices = vertices + 1
    
                    trender.batch = pyglet.graphics.Batch()
                    trender.batch.add(vertices*4, 
                                      pyglet.gl.GL_QUADS, 
                                      pyglet.graphics.TextureGroup(component.tileset_bin.atlas.texture),
                                      ('v2i', vertex_data),
                                      ('t3f', texture_data),
                                      ('c4B', color_data))
                    
                    trender.need_to_update = False


                    
