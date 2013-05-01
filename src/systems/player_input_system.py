# -*- coding: utf-8 -*-

import math

from engine import system

from components import player_input
from components import movement

class PlayerInputSystem(system.System):
    """ Player input system. Handles players inputs. """
    
    def __init__(self, entity_manager=None, keys=None, *args, **kwargs):
        super(PlayerInputSystem, self).__init__(*args, **kwargs)
        
        self.entity_manager = entity_manager
        self.keys = keys
    
    def update(self, dt):
        if self.keys:
            store = self.entity_manager.get_all_components_of_type(player_input.PlayerInput)
    
            if store:
                for entity, component in store.iteritems():
                    move = self.entity_manager.get_component(entity, movement.Movement)

                    if move:
                        if self.keys[component.move_up] and self.keys[component.move_left]:
                            move.rotation = 135
                        elif self.keys[component.move_up] and self.keys[component.move_right]:
                            move.rotation = 45
                        elif self.keys[component.move_down] and self.keys[component.move_left]:
                            move.rotation = 225
                        elif self.keys[component.move_down] and self.keys[component.move_right]:
                            move.rotation = 315
                        elif self.keys[component.move_right]:
                            move.rotation = 0
                        elif self.keys[component.move_left]:
                            move.rotation = 180
                        elif self.keys[component.move_up]:
                            move.rotation = 90
                        elif self.keys[component.move_down]:
                            move.rotation = 270
                            
                        if self.keys[component.move_down] or self.keys[component.move_up] or self.keys[component.move_left] or self.keys[component.move_right]:
                            move.x = move.speed * math.cos(math.radians(move.rotation))
                            move.y = move.speed * math.sin(math.radians(move.rotation))
                        else:
                            move.x = 0
                            move.y = 0
                            
    
    
    