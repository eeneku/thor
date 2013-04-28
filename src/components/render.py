'''
Created on 28.4.2013

@author: eeneku
'''

from engine import component

class Render(component.Component):
    """ Render component. """

    def __init__(self, *args, **kwargs):
        super(Render, self).__init__(*args, **kwargs)
        
        self.image = None