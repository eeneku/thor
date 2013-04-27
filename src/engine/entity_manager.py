'''
Created on 27.4.2013

@author: eeneku
'''

class EntityManager(object):
    """ This class manages all entities in the game. """
    
    def __init__(self, *args, **kwargs):
        self.lowest_unassigned_entity_id = 1
        
        self.entities = []
        self.components = {}
        
    def get_component(self, entity, component):
        store = self.components.get(component.__class__)
        
        if not store:
            print("No entities with component " + component.__class__)
        
        result = store.get(entity)
        
        if not result:
            print("Entity " + entity + " does not posses component " + component.__class__)
        
        return result
    
    def get_all_components_of_type(self, component):
        store = self.components.get(component.__class__)
        
        return_value = []
        
        if store:
            return_value = store.values()
            
        return return_value
    
    def get_all_entities_possessing_component(self, component):
        store = self.components.get(component.__class__)
        
        return_value = {}
        
        if store:
            return_value = store.keys()
            
        return return_value
    
    def add_component(self, entity, component):
        self.components.setdefault(component.__class__, {})[entity] = component()
        
        return component
    
    def create_entity(self):
        new_id = self.lowest_unassigned_entity_id 
        self.entities.append(new_id)
        self.lowest_unassigned_entity_id += 1
        
        return new_id
    
    def kill_entity(self, entity):
        self.entities.remove(entity)