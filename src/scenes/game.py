# -*- coding: utf-8 -*-

import pyglet

from engine import scene
from engine import entity_manager
from engine import system_manager

from components import position
from components import render
from components import movement
from components import player_input
from components import tileset
from components import tilemap

from systems import render_system
from systems import movement_system
from systems import player_input_system
from systems import tilemap_system
from systems import tilemap_render_system

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
        
        self.entity_manager.add_component(self.entity_1, position.Position)
        self.entity_manager.add_component(self.entity_1, render.Render)
        self.entity_manager.add_component(self.entity_1, movement.Movement)
        self.entity_manager.add_component(self.entity_1, player_input.PlayerInput)
        self.entity_manager.add_component(self.entity_2, position.Position)
        self.entity_manager.add_component(self.entity_2, render.Render)
        self.entity_manager.add_component(self.entity_2, movement.Movement)
        
        self.entity_manager.add_component(self.entity_tilemap, tilemap.Tilemap)
        self.entity_manager.add_component(self.entity_tilemap, tileset.Tileset)
        
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
        
        self.entity_manager.get_component(self.entity_2, position.Position).x = 500
        self.entity_manager.get_component(self.entity_2, position.Position).y = 95
        self.entity_manager.get_component(self.entity_2, movement.Movement).y = 16
        self.entity_manager.get_component(self.entity_2, render.Render).image = pyglet.image.load("gfx/ship.png")
        
        self.init_tilemap()
 
        self.render_system = render_system.RenderSystem(self.entity_manager)
        #self.tilemap_render_system = tilemap_render_system.TilemapRenderSystem(self.entity_manager)
        self.system_manager.add_system(movement_system.MovementSystem(self.entity_manager))
        self.system_manager.add_system(player_input_system.PlayerInputSystem(self.entity_manager, self.manager.engine.key_state))
        self.system_manager.add_system(tilemap_system.TilemapSystem(self.entity_manager))
    
    def update(self, dt):
        self.system_manager.update(dt)
            
    def on_draw(self):
        #self.tilemap_render_system.on_draw()
        self.batch.draw()
        self.render_system.on_draw()
        
    def init_tilemap(self):
        height = 20
        width = 39
        
        self.entity_manager.get_component(self.entity_tilemap, tilemap.Tilemap).width = width
        self.entity_manager.get_component(self.entity_tilemap, tilemap.Tilemap).height = height
        self.entity_manager.get_component(self.entity_tilemap, tileset.Tileset).tiles.append(pyglet.image.load("gfx/grass.png"))

        tset = self.entity_manager.get_component(self.entity_tilemap, tileset.Tileset).tiles[0].width
       
        for y in range(0, height):
            for x in range(0, width):
                new_tile = pyglet.sprite.Sprite(self.entity_manager.get_component(self.entity_tilemap, tileset.Tileset).tiles[0])
                new_tile.x = x * tset
                new_tile.y = y * tset
                new_tile.batch = self.batch
                self.entity_manager.get_component(self.entity_tilemap, tilemap.Tilemap).tiles.append(new_tile)
                