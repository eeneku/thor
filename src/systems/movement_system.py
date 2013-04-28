# -*- coding: utf-8 -*-

from engine import system

from components import position
from components import velocity

class MovementSystem(system.System):
    """ Movement system. Draws an image on the screen. """
    
    def __init__(self, entity_manager=None, *args, **kwargs):
        super(MovementSystem, self).__init__(*args, **kwargs)
        
        self.entity_manager = entity_manager
    
    def update(self, dt):
        store = self.entity_manager.get_all_components_of_type(velocity.Velocity)

        if store:
            for entity, component in store.iteritems():
                pos = self.entity_manager.get_component(entity, position.Position)
                
                if pos:
                    pos.x += component.x * dt
                    pos.y += component.y * dt
    
    
    