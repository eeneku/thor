# -*- coding: utf-8 -*-

class SystemManager(object):
    """ This class manages all systems in the game. """
    
    def __init__(self, *args, **kwargs):
        self.systems = []
        
    def add_system(self, system):
        self.systems.append(system)
        
    def update(self, dt):
        for system in self.systems:
            system.update(dt)