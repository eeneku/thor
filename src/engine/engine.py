'''
Created on 27.4.2013

@author: eeneku
'''

import pyglet

class Engine(pyglet.window.Window):
    """ This is the main engine class. """

    def __init__(self, *args, **kwargs):
        super(Engine, self).__init__(*args, **kwargs)
        
        self.fps = pyglet.clock.ClockDisplay()
        
        pyglet.clock.schedule_interval(self.update, 1/120.0)
    
    def run(self):
        pyglet.app.run()
        
    def update(self, dt):
        pass
        
    def on_draw(self):
        self.clear()
        self.fps.draw()