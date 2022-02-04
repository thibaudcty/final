from pathlib import Path
import pygame
import random
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from Euromed.AOE.AOE.definitions import *
import time
class Personnage:
    def __init__(self, tile, world, camera, team):
        self.team = team
        self.world = world
        self.world.entities.append(self)
        self.camera = camera
        self.world.world[tile["grid"][0]][tile["grid"][1]]["entity"]=True
        self.tile = tile
        self.adj_tiles = self.adjacent_tiles(self.tile)

        self.image = pygame.image.load(Path('AOE/assets/Villager/Player/Player_01.png')).convert_alpha()
        self.temp = 0
        self.en_attack = False
        self.moveright_animation = False
        self.moveleft_animation = False
        self.movestraight_animation = False
        self.moveback_animation = False
        self.dead = False
        self.sprites = []
        self.current_sprite = 0
        self.d = 0
        self.avancement = 0
        self.world.workers[tile["grid"][0]][tile["grid"][1]] = self
        self.pos_x = tile["render_pos"][0]
        self.pos_y = tile["render_pos"][1]
        self.selected = False
        self.selected_enemies = []
        self.selection_box = pygame.Rect(self.pos_x + self.world.map_tiles.get_width() / 2 + self.camera.scroll.x + 4,
                                         self.pos_y - self.image.get_height() + self.camera.scroll.y + 34, 24, 34)
        iso_poly = self.tile["iso_poly"] #coord isometrique
        self.iso_poly = None
        self.mouse_to_grid(0, 0, self.camera.scroll)
        self.create_path(tile["grid"][0], tile["grid"][1])
        self.path_index = 0
        self.grids = []


    def adjacent_tiles(self,t):
        return [self.world.world[t["grid"][0]+1][t["grid"][1]]   if (t["grid"][0]+1) < MAP_SIZE                                  else None,   #tile bas gauche
                self.world.world[t["grid"][0]][t["grid"][1]+1]   if (t["grid"][1]+1) < MAP_SIZE                                  else None,   #tile bas droite
                self.world.world[t["grid"][0]-1][t["grid"][1]]   if (t["grid"][0]-1) >= 0                                        else None,   #tile haut gauche
                self.world.world[t["grid"][0]][t["grid"][1]-1]   if (t["grid"][1]-1) >= 0                                        else None,   #tile haut droite
                self.world.world[t["grid"][0]-1][t["grid"][1]-1] if (t["grid"][0]-1) >= 0       and (t["grid"][1]-1) >= 0        else None, #tile haut
                self.world.world[t["grid"][0]+1][t["grid"][1]+1] if (t["grid"][0]+1) > MAP_SIZE and (t["grid"][1]-1) > MAP_SIZE  else None, #tile bas
                self.world.world[t["grid"][0]-1][t["grid"][1]+1] if (t["grid"][0]+1) >= 0       and (t["grid"][1]-1) > MAP_SIZE  else None, #tile droite
                self.world.world[t["grid"][0]+1][t["grid"][1]-1] if (t["grid"][0]+1) > MAP_SIZE and (t["grid"][1]-1) >=0         else None] #tile gauche



    def update_animation(self,speed):
        if self.moveright_animation == True:

            self.current_sprite += speed
        if int(self.current_sprite) >= len(self.sprites):
            self.current_sprite = 0
            self.moveright_animation = False

        elif self.moveleft_animation == True:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
                self.moveleft_animation = False


        elif self.movestraight_animation == True:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
                self.movestraight_animation = False

        elif self.en_attack == True:
            self.current_sprite += speed
            print(self.current_sprite)
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
                self.en_attack = False
        elif self.dead == True:
            self.current_sprite += speed
            print(self.current_sprite)
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
                self.dead = False

        self.image = self.sprites[int(self.current_sprite)]



    def delete(self,unit) :
        self.world.entities.remove(unit)
        self.world.workers[unit.tile["grid"][0]][unit.tile["grid"][1]] = None
        self.world.world[unit.tile["grid"][0]][unit.tile["grid"][1]]["entity"] = False
        unit.world = None

    def close_tile(self,t) :

        for adj_tile in self.adjacent_tiles(t) :
            if adj_tile != None :
                if not adj_tile["collision"] :
                    return adj_tile;
        return None;

    def create_path(self, x, y):
        searching_for_path = True
        while searching_for_path:
            self.dest_tile = self.world.world[x][y]
            if not self.dest_tile["collision"] :
                self.grid = Grid(matrix=self.world.collision_matrix)
                self.start = self.grid.node(self.tile["grid"][0], self.tile["grid"][1])
                self.end = self.grid.node(x, y)
                finder = AStarFinder(diagonal_movement=DiagonalMovement.always)
                self.path_index = 0
                self.path, runs = finder.find_path(self.start, self.end, self.grid)
                searching_for_path = False
            elif self.dest_tile["entity"] :
                if self.close_tile(self.dest_tile) != None :
                    self.dest_tile = self.close_tile(self.dest_tile)
                    self.create_path(self.dest_tile["grid"][0],self.dest_tile["grid"][1])
                break
            else:
                break

    def change_tile(self, new_tile):
        self.world.world[self.tile["grid"][0]][self.tile["grid"][1]]["entity"]=False
        self.world.workers[self.tile["grid"][0]][self.tile["grid"][1]] = None
        self.world.workers[new_tile[0]][new_tile[1]] = self
        self.tile = self.world.world[new_tile[0]][new_tile[1]]
        self.world.world[self.tile["grid"][0]][self.tile["grid"][1]]["entity"]=True
        self.adj_tiles=self.adjacent_tiles(self.tile)

    def mouse_to_grid(self, x, y, scroll):

        world_x = x - scroll.x - self.world.map_tiles.get_width() / 2
        world_y = y - scroll.y
        # transform to cart (inverse of cart_to_iso)
        cart_y = (2 * world_y - world_x) / 2
        cart_x = cart_y + world_x
        # transform to grid coordinates
        grid_x = int(cart_x // TILE_SIZE)
        grid_y = int(cart_y // TILE_SIZE)
        return grid_x, grid_y

    def update(self):

        mx,my = pygame.mouse.get_pos()
        mouse_action = pygame.mouse.get_pressed()
        grid_pos = self.mouse_to_grid(mx, my, self.camera.scroll)

        self.selection_box.update(self.pos_x + self.world.map_tiles.get_width() / 2 + self.camera.scroll.x + 47,
                                  self.pos_y - self.image.get_height() + self.camera.scroll.y + 50, 28, 60)


        pos_poly = [self.pos_x + self.world.map_tiles.get_width() / 2 + self.camera.scroll.x + 47,
                    self.pos_y - self.image.get_height() + self.camera.scroll.y + 50]
        self.iso_poly = [(pos_poly[0] - 10, pos_poly[1] + 44), (pos_poly[0] + 15, pos_poly[1] + 29),
                         (pos_poly[0] + 40, pos_poly[1] + 44), (pos_poly[0] + 15, pos_poly[1] + 59)]


        self.world.collision_matrix[self.tile["grid"][1]][self.tile["grid"][0]] = 0
        self.world.world[self.tile["grid"][0]][self.tile["grid"][1]]["collision"] = True

        # update des animations

        #self.animation_walk_straight()

        if self.selection_box.collidepoint(mx,my):
            if mouse_action[0]:      
                if self.selected == False :
                    self.selected = True
                    self.world.selected_units.append(self)

        if self.selected:
            if mouse_action[2]:
                self.animation_walk_straight()
                if self.team != "enemy" :
                    self.selected_enemies = [unit for unit in self.world.selected_units if unit.team == "enemy"]
                    self.selected = False
                    self.world.selected_units.remove(self)
                    if self.selected_enemies != [] :
                        self.create_path(self.selected_enemies[0].tile["grid"][0], self.selected_enemies[0].tile["grid"][1])
                        #go bagarre
                        #self.animation_attack_straight()
                    else :
                        if len(self.grids) != 0 :
                            self.d = self.direction(grid_pos, self.grids[len(self.grids) - 1])
                            print(self.d)
                        else:
                            self.grids.append(grid_pos)
                            if self.d == 1:
                                self.animation_walk_straight()

                        self.create_path(grid_pos[0], grid_pos[1])
                            
                else :
                    selected_players= [unit for unit in self.world.selected_units if unit.team == "player"]

                    if selected_players == [] :
                        self.selected = False
                        self.world.selected_units.remove(self)

        if self.selected_enemies != [] and not self.world.world[self.selected_enemies[0].tile["grid"][0]][self.selected_enemies[0].tile["grid"][1]]["entity"] :
            self.selected_enemies.pop(0)
            if self.selected_enemies != []:
                self.create_path(self.selected_enemies[0].tile["grid"][0], self.selected_enemies[0].tile["grid"][1])
            else :
                self.create_path(self.tile["grid"][0], self.tile["grid"][1])

        if self.selected_enemies != [] and self.tile in self.selected_enemies[0].adj_tiles and self.world.world[self.selected_enemies[0].tile["grid"][0]][self.selected_enemies[0].tile["grid"][1]]["entity"]:
            self.animation_attack_straight()
            while self.selected_enemies[0].health > 0 :
                self.selected_enemies[0].health = self.selected_enemies[0].health - self.attack
                self.selected_enemies[0].animation_death()

            print("killed it")
            self.delete(self.selected_enemies[0])
            self.selected_enemies.pop(0)
            if self.selected_enemies != []:
                self.create_path(self.selected_enemies[0].tile["grid"][0], self.selected_enemies[0].tile["grid"][1])
            else :
                self.create_path(self.tile["grid"][0], self.tile["grid"][1])

        if self.path_index <= len(self.path) - 1:
            self.movestraight_animation = True
            new_pos = self.path[self.path_index]
            new_real_pos = self.world.world[new_pos[0]][new_pos[1]]["render_pos"]
            if self.avancement < 1:
                self.avancement+= (1 / 135) * 5
                self.avancement = round(self.avancement, 3)
            else:
                self.avancement = 1
            self.pos_x = round(lerp(self.tile["render_pos"][0], new_real_pos[0], self.avancement), 3)
            self.pos_y = round(lerp(self.tile["render_pos"][1], new_real_pos[1], self.avancement), 3)

            if self.pos_x == new_real_pos[0] and self.pos_y == new_real_pos[1]:
                # update position in the world
                self.world.collision_matrix[self.tile["grid"][1]][self.tile["grid"][0]] = 1  # Free the last tile from collision
                self.world.world[self.tile["grid"][0]][self.tile["grid"][1]]["collision"] = False

            if self.pos_x == new_real_pos[0] and self.pos_y == new_real_pos[1]:  # update position in the world
                self.change_tile(new_pos)
                self.path_index += 1
                self.avancement = 0
        else:
            self.movestraight_animation = False
        #self.update_animation(0.2)



class Villageois(Personnage):
    def __init__(self, tile, world, camera):
        super().__init__(tile, world, camera, 'player')
        self.type_perso = "Villageois"
        self.health = 25
        self.attack = 1
        self.costfood = 50
        self.training_time_in_sec = 20
        self.rateoffire = 1.5
        self.speed = 1.1
        # ANIMATION IMAGE WALKING

        self.sprites.append(pygame.image.load(Path('AOE/assets/Villager/Player/Player_01.png')))
        self.image = self.sprites[self.current_sprite]

    def animation_walk_straight(self):
        self.movestraight_animation = True
        self.sprites = []

        self.sprites.append(pygame.image.load(Path('AOE/assets/Villager/Player/Player_01.png')))
        self.sprites.append(pygame.image.load(Path('AOE/assets/Villager/Player/Player_02.png')))
        self.sprites.append(pygame.image.load(Path('AOE/assets/Villager/Player/Player_03.png')))
        self.sprites.append(pygame.image.load(Path('AOE/assets/Villager/Player/Player_04.png')))


    def animation_attack_straight(self):
        self.en_attack = True
        self.sprites = []
        self.sprites.append(pygame.image.load(Path('AOE/assets/Villager/Player/Player_05.png')))
        self.sprites.append(pygame.image.load(Path('AOE/assets/Villager/Player/Player_06.png')))

    def animation_death(self):
        self.dead = True
        self.sprites = []
        self.sprites.append(pygame.image.load(Path('AOE/assets/Villager/Player/Player_07.png')))
        self.sprites.append(pygame.image.load(Path('AOE/assets/Villager/Player/Player_08.png')))


class VillageoisE(Personnage):
    def __init__(self, tile, world, camera):
        super().__init__(tile, world, camera, 'enemy')
        self.type_perso = "VillageoisE"
        self.health = 25
        self.attack = 10
        self.costfood = 50
        self.training_time_in_sec = 20
        self.rateoffire = 1.5
        self.speed = 1.1
        # ANIMATION IMAGE WALKING

        self.sprites.append(pygame.image.load(Path('AOE/assets/Villager/Enemy1/Enemy1.png')))
        self.image = self.sprites[self.current_sprite]

    def animation_walk_straight(self):
        self.movestraight_animation = True
        self.sprites = []

        self.sprites.append(pygame.image.load(Path('AOE/assets/Villager/Enemy1/Enemy1.png')))
        self.sprites.append(pygame.image.load(Path('AOE/assets/Villager/Enemy1/Enemy2.png')))
        self.sprites.append(pygame.image.load(Path('AOE/assets/Villager/Enemy1/Enemy3.png')))
        self.sprites.append(pygame.image.load(Path('AOE/assets/Villager/Enemy1/Enemy4.png')))


    def animation_attack_straight(self):
        self.en_attack = True
        self.sprites = []
        self.sprites.append(pygame.image.load(Path('AOE/assets/Villager/Enemy1/Enemy5.png')))
        self.sprites.append(pygame.image.load(Path('AOE/assets/Villager/Enemy1/Enemy6.png')))

    def animation_death(self):
        self.dead = True
        self.sprites = []
        self.sprites.append(pygame.image.load(Path('AOE/assets/Villager/Enemy1/Enemy7.png')))
        self.sprites.append(pygame.image.load(Path('AOE/assets/Villager/Enemy1/Enemy8.png')))

class Villageois2(Personnage):
    def __init__(self, tile, world, camera):
        super().__init__(tile, world, camera, 'player')
        self.type_perso = "villager"
        self.health = 25
        self.attack = 1
        self.costfood = 50
        self.training_time_in_sec = 20
        self.rateoffire = 1.5
        self.speed = 1.1
        # ANIMATION IMAGE WALKING

        self.sprites.append(pygame.image.load(Path('AOE/assets/Villager/villageois/villager1.png')))
        self.image = self.sprites[self.current_sprite]

    def animation_walk_straight(self):
        self.movestraight_animation = True
        self.sprites = []

        self.sprites.append(pygame.image.load(Path('AOE/assets/Villager/villageois/villager1.png')))
        self.sprites.append(pygame.image.load(Path('AOE/assets/Villager/villageois/villager2.png')))
        self.sprites.append(pygame.image.load(Path('AOE/assets/Villager/villageois/villager3.png')))
        self.sprites.append(pygame.image.load(Path('AOE/assets/Villager/villageois/villager4.png')))


    def animation_attack_straight(self):
        self.en_attack = True
        self.sprites = []
        self.sprites.append(pygame.image.load(Path('AOE/assets/Villager/villageois/villager5.png')))
        self.sprites.append(pygame.image.load(Path('AOE/assets/Villager/villageois/villager6.png')))

    def animation_death(self):
        self.dead = True
        self.sprites = []
        self.sprites.append(pygame.image.load(Path('AOE/assets/Villager/villageois/villager7.png')))
        self.sprites.append(pygame.image.load(Path('AOE/assets/Villager/villageois/villager8.png')))

class tree(Personnage):
    def __init__(self, tile, world, camera):
        super().__init__(tile, world, camera, 'enemy')
        self.type_perso = "tree"
        self.health = 25
        self.attack = 10
        self.costfood = 50
        self.training_time_in_sec = 20
        self.rateoffire = 1.5
        self.speed = 1.1
            # ANIMATION IMAGE WALKING

        self.sprites.append(pygame.image.load(Path('AOE/assets/Villager/treeme.png')))
        self.image = self.sprites[self.current_sprite]

    def animation_walk_straight(self):
        self.movestraight_animation = True
        self.sprites = []

        self.sprites.append(pygame.image.load(Path('AOE/assets/Villager/treeme.png')))
        self.sprites.append(pygame.image.load(Path('AOE/assets/Villager/treeme.png')))
        self.sprites.append(pygame.image.load(Path('AOE/assets/Villager/treeme.png')))
        self.sprites.append(pygame.image.load(Path('AOE/assets/Villager/treeme.png')))

    def animation_attack_straight(self):
        self.en_attack = True
        self.sprites = []
        self.sprites.append(pygame.image.load(Path('AOE/assets/Villager/treeme.png')))
        self.sprites.append(pygame.image.load(Path('AOE/assets/Villager/treeme.png')))

    def animation_death(self):
        self.dead = True
        self.sprites = []
        self.sprites.append(pygame.image.load(Path('AOE/assets/Villager/treeme.png')))
        self.sprites.append(pygame.image.load(Path('AOE/assets/Villager/treeme.png')))