# -*- coding: utf-8 -*-

class EntityManager(object):
    """ This class manages all entities in the game. """
    
    def __init__(self, *args, **kwargs):
        self.lowest_unassigned_entity_id = 1
        
        self.entities = []
        self.components = {}
        
    def get_component(self, entity, component):
        store = self.components.get(component.__name__)
        
        return_value = None
        
        if not store:
            print("No entities with component " + component.__name__)
        else:
            result = store.get(entity)
        
            if not result:
                print("Entity " + entity + " does not posses component " + component.__name__)
            else:
                return_value = result
        
        return return_value
    
    def get_all_components_of_type(self, component):
        return self.components.get(component.__name__)
    
    def get_all_entities_possessing_component(self, component):
        store = self.components.get(component.__name__)
        
        return_value = []
        
        if store:
            return_value = store.keys()
            
        return return_value
    
    def add_component(self, entity, component):
        self.components.setdefault(component.__name__, {})[entity] = component()
        
        return component
    
    def create_entity(self):
        new_id = self.lowest_unassigned_entity_id 
        self.entities.append(new_id)
        self.lowest_unassigned_entity_id += 1
        
        return new_id
    
    def kill_entity(self, entity):
        self.entities.remove(entity)