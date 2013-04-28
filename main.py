# -*- coding: utf-8 -*-

from engine import engine

from scenes import game


class App(object):
    """ The main class that ties everything together. """
    
    def __init__(self):
        self.screen_w = 1280
        self.screen_h = 720
        
        self.engine = engine.Engine(width=self.screen_w, 
                                    height=self.screen_h,
                                    fullscreen=False)
        
        self.engine.scene_manager.add_scene('game', game.Game)
        self.engine.scene_manager.activate_scene('game')
        
        self.engine.run()

if __name__ == '__main__':
    app = App()  