'''
Created on 27.4.2013

@author: eeneku
'''

from engine import component

class Position(component.Component):
    """ Position component."""
    
    def __init__(self, *args, **kwargs):
        super(Position, self).__init__(*kwargs, **kwargs)
        
        self.x = 0
        self.y = 0
        self.z = 0