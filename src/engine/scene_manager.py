# -*- coding: utf-8 -*-

class SceneManager(object):
    """ This class handles the scenes in the game. """

    def __init__(self, engine):
        self.scenes = {}
        self.active_scenes = []
        self.engine = engine

    def add_scene(self, name, scene):
        self.scenes[name] = scene
        
    def activate_scene(self, scene, *args, **kwargs):
        if scene in self.scenes:
            for active_scene in self.active_scenes:
                active_scene.cleanup()
                
            if self.active_scenes:
                self.engine.pop_handlers()
                
            self.active_scenes = []
            
            self.active_scenes.append(self.scenes[scene](self, *args, **kwargs))
            self.engine.push_handlers(self.active_scenes[-1])
            
    def push_scene(self, scene, *args, **kwargs):
        if scene in self.scenes:
            if self.active_scenes:
                self.engine.pop_handlers()
                
            self.active_scenes.append(self.scenes[scene](self, *args, **kwargs))
            self.engine.push_handlers(self.active_scenes[-1])
            
        
    def pop_scene(self):
        if self.active_scenes:
            self.engine.pop_handlers()
            self.active_scenes.pop()
            
            if self.active_scenes:
                self.engine.push_handlers(self.active_scenes[-1])
        
    def update(self, dt):
        if self.active_scenes:
            self.active_scenes[-1].update(dt)
    
    def on_draw(self):
        for scene in self.active_scenes:
            scene.on_draw()