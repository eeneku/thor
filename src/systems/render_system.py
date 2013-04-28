# -*- coding: utf-8 -*-

from engine import system

from components import render
from components import position

class RenderSystem(system.System):
    """ Render system. Draws an image on the screen. """
    
    def __init__(self, entity_manager=None, *args, **kwargs):
        super(RenderSystem, self).__init__(*args, **kwargs)
        
        self.entity_manager = entity_manager
    
    def on_draw(self):
        store = self.entity_manager.get_all_components_of_type(render.Render)

        if store:
            for entity, component in store.iteritems():
                pos = self.entity_manager.get_component(entity, position.Position)
                
                if pos:
                    component.image.blit(pos.x, pos.y)
    
    
    