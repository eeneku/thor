# -*- coding: utf-8 -*-

import pyglet

from pyglet.window import key

from engine import scene
from engine import entity_manager
from engine import system_manager

from components import position
from components import render
from components import movement
from components import player_input
from components import tileset
from components import tilemap
from components import tilemap_render

from systems import render_system
from systems import movement_system
from systems import player_input_system
from systems import tilemap_system
from systems import tilemap_render_system

from utils import tilemap_loader

class Game(scene.Scene):
    """ The main scene where most of the game is happening. """

    def __init__(self, manager):
        super(Game, self).__init__(manager)
        
        self.batch = pyglet.graphics.Batch()
        
        self.entity_manager = entity_manager.EntityManager()
        self.system_manager = system_manager.SystemManager()
        
        self.entity_1 = self.entity_manager.create_entity()
        self.entity_2 = self.entity_manager.create_entity()
        self.entity_tilemap = self.entity_manager.create_entity()
        self.entity_3 = self.entity_manager.create_entity()
        self.entity_4 = self.entity_manager.create_entity()
        self.entity_5 = self.entity_manager.create_entity()
        self.entity_6 = self.entity_manager.create_entity()
        
        self.entity_manager.add_component(self.entity_1, position.Position)
        self.entity_manager.add_component(self.entity_1, render.Render)
        self.entity_manager.add_component(self.entity_1, movement.Movement)
        self.entity_manager.add_component(self.entity_1, player_input.PlayerInput)
        self.entity_manager.add_component(self.entity_2, position.Position)
        self.entity_manager.add_component(self.entity_2, render.Render)
        self.entity_manager.add_component(self.entity_2, movement.Movement)
        
        self.entity_manager.add_component(self.entity_tilemap, tilemap.Tilemap)
        self.entity_manager.add_component(self.entity_tilemap, tileset.Tileset)
        self.entity_manager.add_component(self.entity_tilemap, tilemap_render.TilemapRender)
        
        self.entity_manager.add_component(self.entity_3, position.Position)
        self.entity_manager.add_component(self.entity_3, render.Render)
        self.entity_manager.add_component(self.entity_4, position.Position)
        self.entity_manager.add_component(self.entity_4, render.Render)
        self.entity_manager.add_component(self.entity_5, position.Position)
        self.entity_manager.add_component(self.entity_5, render.Render)
        self.entity_manager.add_component(self.entity_6, position.Position)
        self.entity_manager.add_component(self.entity_6, render.Render)
        
        self.entity_manager.get_component(self.entity_1, position.Position).x = 99
        self.entity_manager.get_component(self.entity_1, position.Position).y = 150
        self.entity_manager.get_component(self.entity_1, movement.Movement).x = 0
        self.entity_manager.get_component(self.entity_1, movement.Movement).y = 0
        self.entity_manager.get_component(self.entity_1, movement.Movement).speed = 128
        self.entity_manager.get_component(self.entity_1, render.Render).image = pyglet.image.load("gfx/asteroid.png")
        self.entity_manager.get_component(self.entity_1, player_input.PlayerInput).move_up = 65362
        self.entity_manager.get_component(self.entity_1, player_input.PlayerInput).move_down = 65364
        self.entity_manager.get_component(self.entity_1, player_input.PlayerInput).move_left = 65361
        self.entity_manager.get_component(self.entity_1, player_input.PlayerInput).move_right = 65363
        
        img = pyglet.image.load("gfx/bullet.png")
        self.entity_manager.get_component(self.entity_3, position.Position).x = 150
        self.entity_manager.get_component(self.entity_3, position.Position).y = 620
        self.entity_manager.get_component(self.entity_3, render.Render).image = img
        self.entity_manager.get_component(self.entity_4, position.Position).x = 150
        self.entity_manager.get_component(self.entity_4, position.Position).y = 120
        self.entity_manager.get_component(self.entity_4, render.Render).image = img
        self.entity_manager.get_component(self.entity_5, position.Position).x = 650
        self.entity_manager.get_component(self.entity_5, position.Position).y = 620
        self.entity_manager.get_component(self.entity_5, render.Render).image = img
        self.entity_manager.get_component(self.entity_6, position.Position).x = 650
        self.entity_manager.get_component(self.entity_6, position.Position).y = 120
        self.entity_manager.get_component(self.entity_6, render.Render).image = img
        
        self.entity_manager.get_component(self.entity_2, position.Position).x = 0
        self.entity_manager.get_component(self.entity_2, position.Position).y = 0
        self.entity_manager.get_component(self.entity_2, movement.Movement).y = 0
        self.entity_manager.get_component(self.entity_2, render.Render).image = pyglet.image.load("gfx/ship.png")
        
        self.init_tilemap()
 
        self.render_system = render_system.RenderSystem(self.entity_manager)
        self.system_manager.add_system(tilemap_render_system.TilemapRenderSystem(self.entity_manager))
        self.system_manager.add_system(movement_system.MovementSystem(self.entity_manager))
        self.system_manager.add_system(player_input_system.PlayerInputSystem(self.entity_manager, self.manager.engine.key_state))
        self.system_manager.add_system(tilemap_system.TilemapSystem(self.entity_manager))
    
    def update(self, dt):
        if self.manager.engine.key_state[key.UP]:
            self.entity_manager.get_component(self.entity_tilemap, tilemap_render.TilemapRender).world_y -= 128 * dt
        if self.manager.engine.key_state[key.DOWN]:
            self.entity_manager.get_component(self.entity_tilemap, tilemap_render.TilemapRender).world_y += 128 * dt
        if self.manager.engine.key_state[key.RIGHT]:
            self.entity_manager.get_component(self.entity_tilemap, tilemap_render.TilemapRender).world_x -= 128 * dt
        if self.manager.engine.key_state[key.LEFT]:
            self.entity_manager.get_component(self.entity_tilemap, tilemap_render.TilemapRender).world_x += 128 * dt
            
        self.entity_manager.get_component(self.entity_tilemap, tilemap_render.TilemapRender).need_to_update = True
        self.system_manager.update(dt)
            
    def on_draw(self):
        self.batch.draw()
        self.render_system.on_draw()

        
    def init_tilemap(self):
        tilemap_loader.tilemap_loader("test2.tmx",
                                      self.entity_manager.get_component(self.entity_tilemap, tilemap.Tilemap),
                                      self.entity_manager.get_component(self.entity_tilemap, tileset.Tileset),
                                      self.batch)

                