import pygame
import random
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from Euromed.AOE.AOE.definitions import *

class IApersonnage:
    def __init__(self, tile, world,camera):
        self.world = world
        self.world.entities.append(self)
        self.tile = tile
        self.camera = camera
        self.current_sprite = 0
        self.pos_x = tile["render_pos"][0]
        self.pos_y = tile["render_pos"][1]
        self.iso_poly = None
        self.sprites = []
        #pathfinding
        self.world.iaworkers[tile["grid"][0]][tile["grid"][1]] = self
        self.move_timer = pygame.time.get_ticks()
        self.movestraight_animation = False
        self.path_index = 0
        #self.path = []
        x = random.randint(0, self.world.grid_length_x - 1)
        y = random.randint(0, self.world.grid_length_y - 1)
        self.grid = Grid(matrix=self.world.collision_matrix)
        self.start = self.grid.node(self.tile["grid"][0], self.tile["grid"][1])
        self.end = self.grid.node(x, y)
        finder = AStarFinder(diagonal_movement=DiagonalMovement.always)
        self.path_index = 0
        self.path, runs = finder.find_path(self.start, self.end, self.grid)



    def update_animation(self, speed):

        if self.movestraight_animation == True:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
                self.movestraight_animation = False



    def create_path(self):
        searching_for_path = True
        while searching_for_path:
            x = random.randint(0 , self.world.grid_length_x - 1)
            y = random.randint(0, self.world.grid_length_y - 1)
            self.dest_tile = self.world.world[x][y]
            if not self.dest_tile["collision"]:
                self.grid = Grid(matrix=self.world.collision_matrix)
                self.start = self.grid.node(self.tile["grid"][0], self.tile["grid"][1])
                self.end = self.grid.node(x, y)
                finder = AStarFinder(diagonal_movement=DiagonalMovement.always)
                self.path_index = 0
                self.path, runs = finder.find_path(self.start, self.end, self.grid)
                for e in self.path :
                    print(e)
                searching_for_path = False
            else:
                break

    def change_tile(self, new_tile):
        self.world.iaworkers[self.tile["grid"][0]][self.tile["grid"][1]] = None
        self.world.iaworkers[new_tile[0]][new_tile[1]] = self
        self.tile = self.world.world[new_tile[0]][new_tile[1]]
    def update(self):
        pos_poly = [self.pos_x + self.world.map_tiles.get_width() / 2 + self.camera.scroll.x + 47,
                    self.pos_y - self.image.get_height() + self.camera.scroll.y + 50]
        self.iso_poly = [(pos_poly[0] - 10, pos_poly[1] + 44), (pos_poly[0] + 15, pos_poly[1] + 29),
                         (pos_poly[0] + 40, pos_poly[1] + 44), (pos_poly[0] + 15, pos_poly[1] + 59)]
        now = pygame.time.get_ticks()
        if now - self.move_timer > 2000 :
            try:
                new_pos = self.path[self.path_index]
                self.update_animation(0.2)
                self.animation_walk_straight()
                self.change_tile(new_pos)
                self.path_index += 1
                self.move_timer = now
                if self.path_index == len(self.path) - 1 :
                    self.create_path()
            except:
                print("error path")
class ENEMY(IApersonnage):
    def __init__(self, tile, world, camera):
            super().__init__(tile, world, camera)
            self.type_perso = "ENEMY"
            self.health = 35
            self.attack = 3
            self.costfood = 50
            self.training_time_in_sec = 30
            self.rateoffire = 1.4
            self.range = 5
            self.speed = 1.2
            self.upgradecost = 100
            self.upgrade_time_in_sec = 40

            # ANIMATION IMAGE WALK
            self.sprites.append(pygame.image.load('AOE/assets/Villager/Enemy/Enemy_01.png'))
            self.image = self.sprites[self.current_sprite]

    def animation_walk_straight(self):
            self.movestraight_animation = True
            self.sprites = []
            self.sprites.append(pygame.image.load('AOE/assets/Villager/Enemy/Enemy_01.png'))
            self.sprites.append(pygame.image.load('AOE/assets/Villager/Enemy/Enemy_02.png'))
            self.sprites.append(pygame.image.load('AOE/assets/Villager/Enemy/Enemy_03.png'))
            self.sprites.append(pygame.image.load('AOE/assets/Villager/Enemy/Enemy_04.png'))
            self.sprites.append(pygame.image.load('AOE/assets/Villager/Enemy/Enemy_05.png'))
            self.sprites.append(pygame.image.load('AOE/assets/Villager/Enemy/Enemy_06.png'))
            self.sprites.append(pygame.image.load('AOE/assets/Villager/Enemy/Enemy_07.png'))
            self.sprites.append(pygame.image.load('AOE/assets/Villager/Enemy/Enemy_08.png'))


class ANIMAL(IApersonnage):
    def __init__(self, tile, world, camera):
        super().__init__( tile, world, camera)
        self.type_perso = "ANIMAL"
        self.health = 35
        self.attack = 3
        self.costfood = 50
        self.training_time_in_sec = 30
        self.rateoffire = 1.4
        self.range = 5
        self.speed = 1.2
        self.upgradecost = 100
        self.upgrade_time_in_sec = 40

        # ANIMATION IMAGE WALK
        self.sprites.append(pygame.image.load('AOE/assets/Villager/Animal/horse01.png'))
        self.image = self.sprites[self.current_sprite]

    def animation_walk_straight(self):
        self.movestraight_animation = True
        self.sprites = []
        self.sprites.append(pygame.image.load('AOE/assets/Villager/Animal/horse01.png'))
        self.sprites.append(pygame.image.load('AOE/assets/Villager/Animal/horse02.png'))
        self.sprites.append(pygame.image.load('AOE/assets/Villager/Animal/horse03.png'))
        self.sprites.append(pygame.image.load('AOE/assets/Villager/Animal/horse04.png'))
        self.sprites.append(pygame.image.load('AOE/assets/Villager/Animal/horse05.png'))
        self.sprites.append(pygame.image.load('AOE/assets/Villager/Animal/horse06.png'))
        self.sprites.append(pygame.image.load('AOE/assets/Villager/Animal/horse07.png'))
        self.sprites.append(pygame.image.load('AOE/assets/Villager/Animal/horse08.png'))
        self.sprites.append(pygame.image.load('AOE/assets/Villager/Animal/horse09.png'))
        self.sprites.append(pygame.image.load('AOE/assets/Villager/Animal/horse10.png'))
        self.sprites.append(pygame.image.load('AOE/assets/Villager/Animal/horse11.png'))
        self.sprites.append(pygame.image.load('AOE/assets/Villager/Animal/horse12.png'))


class SHEEP(IApersonnage):
    def __init__(self, tile, world, camera):
        super().__init__( tile, world, camera)
        self.type_perso = "SHEEP"
        self.health = 35
        self.attack = 3
        self.costfood = 50
        self.training_time_in_sec = 30
        self.rateoffire = 1.4
        self.range = 5
        self.speed = 1.2
        self.upgradecost = 100
        self.upgrade_time_in_sec = 40

        # ANIMATION IMAGE WALK
        self.sprites.append(pygame.image.load('AOE/assets/Villager/Sheep/mouton01.png'))
        self.image = self.sprites[self.current_sprite]

    def animation_walk_straight(self):
        self.movestraight_animation = True
        self.sprites = []
        self.sprites.append(pygame.image.load('AOE/assets/Villager/Sheep/mouton01.png'))
        self.sprites.append(pygame.image.load('AOE/assets/Villager/Sheep/mouton02.png'))
        self.sprites.append(pygame.image.load('AOE/assets/Villager/Sheep/mouton03.png'))
        self.sprites.append(pygame.image.load('AOE/assets/Villager/Sheep/mouton04.png'))
        self.sprites.append(pygame.image.load('AOE/assets/Villager/Sheep/mouton05.png'))
        self.sprites.append(pygame.image.load('AOE/assets/Villager/Sheep/mouton06.png'))
        self.sprites.append(pygame.image.load('AOE/assets/Villager/Sheep/mouton07.png'))
        self.sprites.append(pygame.image.load('AOE/assets/Villager/Sheep/mouton08.png'))
        self.sprites.append(pygame.image.load('AOE/assets/Villager/Sheep/mouton09.png'))
        self.sprites.append(pygame.image.load('AOE/assets/Villager/Sheep/mouton010.png'))
        self.sprites.append(pygame.image.load('AOE/assets/Villager/Sheep/mouton011.png'))
        self.sprites.append(pygame.image.load('AOE/assets/Villager/Sheep/mouton012.png'))
