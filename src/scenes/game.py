# -*- coding: utf-8 -*-

from pyglet import image

from engine import scene
from engine import entity_manager
from engine import system_manager

from components import position
from components import render
from components import velocity

from systems import render_system
from systems import movement_system

class Game(scene.Scene):
    """ The main scene where most of the game is happening. """

    def __init__(self, manager):
        super(Game, self).__init__(manager)
        
        self.entity_manager = entity_manager.EntityManager()
        self.system_manager = system_manager.SystemManager()
        
        self.entity_1 = self.entity_manager.create_entity()
        self.entity_2 = self.entity_manager.create_entity()
        
        self.entity_manager.add_component(self.entity_1, position.Position)
        self.entity_manager.add_component(self.entity_1, render.Render)
        self.entity_manager.add_component(self.entity_1, velocity.Velocity)
        self.entity_manager.add_component(self.entity_2, position.Position)
        self.entity_manager.add_component(self.entity_2, render.Render)
        self.entity_manager.add_component(self.entity_2, velocity.Velocity)
        
        self.entity_manager.get_component(self.entity_1, position.Position).x = 99
        self.entity_manager.get_component(self.entity_1, position.Position).y = 150
        self.entity_manager.get_component(self.entity_1, velocity.Velocity).x = 16
        self.entity_manager.get_component(self.entity_1, velocity.Velocity).y = 32
        self.entity_manager.get_component(self.entity_1, render.Render).image = image.load("gfx/asteroid.png")
        
        self.entity_manager.get_component(self.entity_2, position.Position).x = 500
        self.entity_manager.get_component(self.entity_2, position.Position).y = 95
        self.entity_manager.get_component(self.entity_2, velocity.Velocity).y = 16
        self.entity_manager.get_component(self.entity_2, render.Render).image = image.load("gfx/ship.png")
        
        self.render_system = render_system.RenderSystem(self.entity_manager)
        self.system_manager.add_system(movement_system.MovementSystem(self.entity_manager))
    
    def update(self, dt):
        self.system_manager.update(dt)
            
    def on_draw(self):
        self.render_system.on_draw()