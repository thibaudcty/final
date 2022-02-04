import os
from Euromed.AOE.AOE.game import *
from Euromed.AOE.AOE.definitions import *
from pygame import *


import os

#to get the current working directory
directory = os.getcwd()

print(directory)
def main():
    running = True
    playing = True
    pygame.init()
    pygame.mixer.init() #son a implementer 
    SCREEN = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    clock = pygame.time.Clock()


    #implement game
    game = Game(SCREEN,clock)
    while running:

        while playing:

           game.run()

#La fonction main() ne doit etre appelée que si on execute main.py, pas dans un autre fichier.py
if __name__ == "__main__":
    main()            










