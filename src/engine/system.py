# -*- coding: utf-8 -*-

class System(object):
    """ This is the father class for all different systems. """
    
    def __init__(self, *args, **kwargs):
        pass

    def update(self, dt):
        raise NotImplementedError
    