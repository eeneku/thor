from engine import engine
from engine import entity_manager
from components import position

class App(object):
    """ The main class that ties everything together. """
    
    def __init__(self):
        self.screen_w = 1280
        self.screen_h = 720
        
        self.engine = engine.Engine(width=self.screen_w, 
                                    height=self.screen_h,
                                    fullscreen=False)
        
        self.entity_manager = entity_manager.EntityManager()
        
        self.entity_1 = self.entity_manager.create_entity()
        
        self.entity_manager.add_component(self.entity_1, position.Position)
        
        print(self.entity_manager.entities)
        print(self.entity_manager.components)
        print(self.entity_manager.get_component(self.entity_1, position.Position).x)
        
        self.entity_manager.get_component(self.entity_1, position.Position).x = 99
        
        print(self.entity_manager.get_component(self.entity_1, position.Position).x)
        
        print(self.entity_manager.get_all_entities_possessing_component(position.Position))
        
        print(self.entity_manager.get_all_components_of_type(position.Position))
        
        self.engine.run()

if __name__ == '__main__':
    app = App()  