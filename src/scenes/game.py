# -*- coding: utf-8 -*-

from pyglet import image
from pyglet.window import key

from engine import scene
from engine import entity_manager
from engine import system_manager

from components import position
from components import render
from components import movement
from components import player_input

from systems import render_system
from systems import movement_system
from systems import player_input_system

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
        self.entity_manager.add_component(self.entity_1, movement.Movement)
        self.entity_manager.add_component(self.entity_1, player_input.PlayerInput)
        self.entity_manager.add_component(self.entity_2, position.Position)
        self.entity_manager.add_component(self.entity_2, render.Render)
        self.entity_manager.add_component(self.entity_2, movement.Movement)
        
        self.entity_manager.get_component(self.entity_1, position.Position).x = 99
        self.entity_manager.get_component(self.entity_1, position.Position).y = 150
        self.entity_manager.get_component(self.entity_1, movement.Movement).x = 0
        self.entity_manager.get_component(self.entity_1, movement.Movement).y = 0
        self.entity_manager.get_component(self.entity_1, movement.Movement).speed = 128
        self.entity_manager.get_component(self.entity_1, render.Render).image = image.load("gfx/asteroid.png")
        self.entity_manager.get_component(self.entity_1, player_input.PlayerInput).move_up = 65362
        self.entity_manager.get_component(self.entity_1, player_input.PlayerInput).move_down = 65364
        self.entity_manager.get_component(self.entity_1, player_input.PlayerInput).move_left = 65361
        self.entity_manager.get_component(self.entity_1, player_input.PlayerInput).move_right = 65363
        
        self.entity_manager.get_component(self.entity_2, position.Position).x = 500
        self.entity_manager.get_component(self.entity_2, position.Position).y = 95
        self.entity_manager.get_component(self.entity_2, movement.Movement).y = 16
        self.entity_manager.get_component(self.entity_2, render.Render).image = image.load("gfx/ship.png")
        
        self.render_system = render_system.RenderSystem(self.entity_manager)
        self.system_manager.add_system(movement_system.MovementSystem(self.entity_manager))
        self.system_manager.add_system(player_input_system.PlayerInputSystem(self.entity_manager, self.manager.engine.key_state))
    
    def update(self, dt):
        self.system_manager.update(dt)
            
    def on_draw(self):
        self.render_system.on_draw()