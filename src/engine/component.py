'''
Created on 25.4.2013

@author: eeneku
'''

class Component(object):
    """ This is the father class for all different components. """
    
    def __init__(self,*args, **kwargs):
        pass
    
    def get_type(self):
        
        raise NotImplementedError