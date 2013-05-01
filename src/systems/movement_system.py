# -*- coding: utf-8 -*-

from engine import system

from components import position
from components import movement

class MovementSystem(system.System):
    """ Movement system. Moves the entity around. """
    
    def __init__(self, entity_manager=None, *args, **kwargs):
        super(MovementSystem, self).__init__(*args, **kwargs)
        
        self.entity_manager = entity_manager
    
    def update(self, dt):
        store = self.entity_manager.get_all_components_of_type(movement.Movement)

        if store:
            for entity, component in store.iteritems():
                pos = self.entity_manager.get_component(entity, position.Position)
                
                if pos:
                    pos.x += component.x * dt
                    pos.y += component.y * dt
    
    
    