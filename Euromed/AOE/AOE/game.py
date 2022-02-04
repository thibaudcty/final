#import pygame
import sys
#from definitions import *
from Euromed.AOE.AOE.world import World
from Euromed.AOE.AOE.camera import Camera



from Euromed.AOE.AOE.hud import *
from Euromed.AOE.AOE.worker import *
from Euromed.AOE.AOE.IA import *
from Euromed.AOE.AOE.resource_manager import ResourceManager
#from ecran_daccueil import *
####VARIABLES GLOBALES


class Game:
    def __init__(self, screen, clock):

        pygame.init()
        self.running,self.playing = True,False

        self.screen = screen
        self.clock = clock
        self.width, self.height = self.screen.get_size()

        self.entities = []


        # resource manager
        self.resource_manager = ResourceManager()
        # hud
        self.hud = Hud(self.resource_manager,self.width, self.height)
        #World
        self.world = World(self.resource_manager,self.entities,self.hud,MAP_SIZE,MAP_SIZE,self.width,self.height)

        #Camera
        self.camera = Camera(self.width, self.height)


    #killer
        #Villageois(self.world.world[25][15], self.world, self.camera)
        #illageois(self.world.world[30][18], self.world, self.camera)
        #Villageois(self.world.world[15][10], self.world, self.camera)
        #Villageois(self.world.world[20][-3], self.world, self.camera)
        #Villageois(self.world.world[30][1], self.world, self.camera)
        #Villageois(self.world.world[10][9], self.world, self.camera)
        #Villageois(self.world.world[35][-4], self.world, self.camera)
        Villageois(self.world.world[33][4], self.world, self.camera)
        Villageois(self.world.world[25][15], self.world, self.camera)
        Villageois(self.world.world[30][18], self.world, self.camera)
        Villageois(self.world.world[15][10], self.world, self.camera)
        Villageois(self.world.world[20][-3], self.world, self.camera)
        Villageois(self.world.world[30][1], self.world, self.camera)
        Villageois(self.world.world[10][9], self.world, self.camera)
        Villageois(self.world.world[35][-4], self.world, self.camera)
        Villageois(self.world.world[23][6], self.world, self.camera)
        Villageois(self.world.world[15][1], self.world, self.camera)
        Villageois(self.world.world[7][14], self.world, self.camera)
        Villageois(self.world.world[9][15], self.world, self.camera)
        Villageois(self.world.world[26][32], self.world, self.camera)
        Villageois(self.world.world[28][35], self.world, self.camera)
        Villageois(self.world.world[17][22], self.world, self.camera)


#ennemy
        VillageoisE(self.world.world[20][8], self.world, self.camera)
        #VillageoisE(self.world.world[30][3], self.world, self.camera)
        #VillageoisE(self.world.world[30][7], self.world, self.camera)
        #VillageoisE(self.world.world[40][-3], self.world, self.camera)
        VillageoisE(self.world.world[35][7], self.world, self.camera)
        VillageoisE(self.world.world[35][8], self.world, self.camera)
        VillageoisE(self.world.world[20][-5], self.world, self.camera)
        VillageoisE(self.world.world[10][7], self.world, self.camera)

        VillageoisE(self.world.world[25][4], self.world, self.camera)
        VillageoisE(self.world.world[30][3], self.world, self.camera)
        VillageoisE(self.world.world[30][7], self.world, self.camera)
        VillageoisE(self.world.world[40][-3], self.world, self.camera)
        VillageoisE(self.world.world[20][-7], self.world, self.camera)
        VillageoisE(self.world.world[35][28], self.world, self.camera)
        VillageoisE(self.world.world[27][-5], self.world, self.camera)
        VillageoisE(self.world.world[24][17], self.world, self.camera)
        VillageoisE(self.world.world[20][7], self.world, self.camera)
        VillageoisE(self.world.world[42][14], self.world, self.camera)
        VillageoisE(self.world.world[15][-4], self.world, self.camera)
        VillageoisE(self.world.world[4][-3], self.world, self.camera)
        VillageoisE(self.world.world[11][-2], self.world, self.camera)
        VillageoisE(self.world.world[10][-1], self.world, self.camera)
        VillageoisE(self.world.world[9][9], self.world, self.camera)



#pos1
        tree(self.world.world[68][3], self.world, self.camera)
        tree(self.world.world[68][5], self.world, self.camera)
        tree(self.world.world[70][3], self.world, self.camera)
        tree(self.world.world[70][5], self.world, self.camera)
        #tree(self.world.world[20][-3], self.world, self.camera)

        tree(self.world.world[50][10], self.world, self.camera)
        tree(self.world.world[50][12], self.world, self.camera)
        tree(self.world.world[52][10], self.world, self.camera)
        tree(self.world.world[52][12], self.world, self.camera)

        tree(self.world.world[20][-10], self.world, self.camera)
        tree(self.world.world[20][-11], self.world, self.camera)
        tree(self.world.world[21][-12], self.world, self.camera)
        tree(self.world.world[21][-5], self.world, self.camera)
        tree(self.world.world[19][-3], self.world, self.camera)
        tree(self.world.world[19][-4], self.world, self.camera)
        #tree(self.world.world[19][-5], self.world, self.camera)
        #tree(self.world.world[19][-2], self.world, self.camera)
#pos2

        tree(self.world.world[21][3], self.world, self.camera)
        tree(self.world.world[21][4], self.world, self.camera)
        tree(self.world.world[20][2], self.world, self.camera)
        tree(self.world.world[20][3], self.world, self.camera)
        tree(self.world.world[20][4], self.world, self.camera)
        tree(self.world.world[20][5], self.world, self.camera)
        tree(self.world.world[21][2], self.world, self.camera)
        tree(self.world.world[21][5], self.world, self.camera)
        tree(self.world.world[19][3], self.world, self.camera)
        tree(self.world.world[19][4], self.world, self.camera)
        tree(self.world.world[19][5], self.world, self.camera)
        tree(self.world.world[19][2], self.world, self.camera)

#pos3
        tree(self.world.world[21][21], self.world, self.camera)
        tree(self.world.world[21][20], self.world, self.camera)
        tree(self.world.world[20][19], self.world, self.camera)
        tree(self.world.world[20][20], self.world, self.camera)
        tree(self.world.world[20][21], self.world, self.camera)
        tree(self.world.world[20][22], self.world, self.camera)
        tree(self.world.world[21][19], self.world, self.camera)
        tree(self.world.world[21][22], self.world, self.camera)
        tree(self.world.world[19][19], self.world, self.camera)
        tree(self.world.world[19][20], self.world, self.camera)
        tree(self.world.world[19][21], self.world, self.camera)
        tree(self.world.world[19][22], self.world, self.camera)

#cavalier
        ENEMY(self.world.world[20][35],self.world,self.camera)
        ENEMY(self.world.world[20][25], self.world, self.camera)
        ENEMY(self.world.world[25][15], self.world, self.camera)
        ENEMY(self.world.world[10][5], self.world, self.camera)


#villager
        Villageois2(self.world.world[10][13], self.world, self.camera)
        Villageois2(self.world.world[39][-5], self.world, self.camera)
        Villageois2(self.world.world[30][19], self.world, self.camera)
        Villageois2(self.world.world[40][45], self.world, self.camera)
        Villageois2(self.world.world[26][30], self.world, self.camera)
        Villageois2(self.world.world[20][22], self.world, self.camera)
        Villageois2(self.world.world[26][-10], self.world, self.camera)
        Villageois2(self.world.world[49][22], self.world, self.camera)
        Villageois2(self.world.world[19][19], self.world, self.camera)
    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()



    def events(self):
        for event in pygame.event.get(): # Si on clique sur la croix pour quitter, on arrete le jeu
            mx, my = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                self.running,self.playing = False,False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()


    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False,False,False,False

    def update(self):
        self.camera.update()
        self.hud.update()
        self.world.update(self.camera)
        # self.player.update()
        for e in self.entities :
            e.update_animation(0.2)
            e.update()


    def draw(self): #Construction graphiques
        self.screen.fill(BLACK)  # Arrière plan
        self.world.draw(self.screen,self.camera)
        self.hud.draw(self.screen)
        # self.player
        pygame.display.flip()

