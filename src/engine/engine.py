# -*- coding: utf-8 -*-

import pyglet

import scene_manager

class Engine(pyglet.window.Window):
    """ This is the main engine class. """

    def __init__(self, *args, **kwargs):
        super(Engine, self).__init__(*args, **kwargs)
        
        self.scene_manager = scene_manager.SceneManager(engine=self)
        self.fps = pyglet.clock.ClockDisplay()
        
        self.key_state = pyglet.window.key.KeyStateHandler()
        self.push_handlers(self.key_state)
        
        pyglet.clock.schedule_interval(self.update, 1/120.0)
        
    def run(self):
        pyglet.app.run()
        
    def update(self, dt):
        self.scene_manager.update(dt)
        
    def on_draw(self):
        self.clear()
        self.scene_manager.on_draw()
        self.fps.draw()