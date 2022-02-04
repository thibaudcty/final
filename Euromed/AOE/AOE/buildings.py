
import pygame

class towncenter:

    def __init__(self, pos, team,resource_manager):
        self.image = pygame.image.load("AOE/assets/Towncenter.png")
        self.name = "Towncenter"
        self.rect = self.image.get_rect(topleft=pos)
        self.resource_manager = resource_manager
        self.resource_manager.apply_cost_to_resource(self.name)
        self.resource_cooldown = pygame.time.get_ticks()
        self.counter = 300
        self.team = team

    def update(self):

        pass
    def update_animation(self,speed):
        pass


class maison:

    def __init__(self, pos, team,resource_manager):
        self.image = pygame.image.load("AOE/Buildings/House1.png")
        self.name = "House"
        self.rect = self.image.get_rect(topleft=pos)
        self.resource_manager = resource_manager
        self.resource_manager.apply_cost_to_resource(self.name)
        self.resource_cooldown = pygame.time.get_ticks()
        self.counter = 300
        self.team = team

    def update(self):

        pass

    def update_animation(self,speed):
        pass

class castle:

    def __init__(self, pos, team, resource_manager):
        self.image = pygame.image.load("AOE/assets/castle.png")
        self.name = "castle"
        self.rect = self.image.get_rect(topleft=pos)
        self.resource_manager = resource_manager
        self.resource_manager.apply_cost_to_resource(self.name)
        self.resource_cooldown = pygame.time.get_ticks()
        self.counter = 300
        self.team = team

    def update(self):
        # self.counter += 1
        pass

    def update_animation(self, speed):
        pass

    def update_animation(self, speed):
            pass

class moulin:

    def __init__(self, pos, team, resource_manager):
        self.image = pygame.image.load("AOE/assets/moulin.png")
        self.name = "moulin"
        self.rect = self.image.get_rect(topleft=pos)
        self.resource_manager = resource_manager
        self.resource_manager.apply_cost_to_resource(self.name)
        self.resource_cooldown = pygame.time.get_ticks()
        self.counter = 300
        self.team = team

    def update(self):

        pass

    def update_animation(self, speed):
            pass

class sheep:

    def __init__(self, pos, team, resource_manager):
        self.image = pygame.image.load("AOE/assets/Animals/sheep.png")
        self.name = "Sheep"
        self.rect = self.image.get_rect(topleft=pos)
        self.resource_manager = resource_manager
        self.resource_manager.apply_cost_to_resource(self.name)
        self.resource_cooldown = pygame.time.get_ticks()
        self.counter = 300
        self.team = team

    def update(self):
        pass

    def update_animation(self, speed):
        pass

class horse:

    def __init__(self, pos, team, resource_manager):
        self.image = pygame.image.load("AOE/assets/Animals/horse.png")
        self.name = "Horse"
        self.rect = self.image.get_rect(topleft=pos)
        self.resource_manager = resource_manager
        self.resource_manager.apply_cost_to_resource(self.name)
        self.resource_cooldown = pygame.time.get_ticks()
        self.counter = 300
        self.team = team

    def update(self):
        pass

    def update_animation(self, speed):
        pass

class goat:

    def __init__(self, pos, team, resource_manager):
        self.image = pygame.image.load("AOE/assets/Animals/goat.png")
        self.name = "Goat"
        self.rect = self.image.get_rect(topleft=pos)
        self.resource_manager = resource_manager
        self.resource_manager.apply_cost_to_resource(self.name)
        self.resource_cooldown = pygame.time.get_ticks()
        self.counter = 300
        self.team = team

    def update(self):
        pass

    def update_animation(self, speed):
        pass

class chicken:

    def __init__(self, pos, team, resource_manager):
        self.image = pygame.image.load("AOE/assets/Animals/chiken.png")
        self.name = "Chicken"
        self.rect = self.image.get_rect(topleft=pos)
        self.resource_manager = resource_manager
        self.resource_manager.apply_cost_to_resource(self.name)
        self.resource_cooldown = pygame.time.get_ticks()
        self.counter = 300
        self.team = team

    def update(self):
        pass

    def update_animation(self, speed):
        pass