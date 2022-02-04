import pygame

import Euromed.AOE.menu.Replay
import Euromed.AOE.menu.Test
import Euromed.AOE.menu.Test2
import Euromed.AOE.menu.Test3
from Euromed.AOE.menu.Menu_principal import *
import Euromed.AOE.menu.Nouveau_match
import Euromed.AOE.menu.Reprendre_match
import Euromed.AOE.menu.Bibliotheque
import Euromed.AOE.menu.Menu_principal
import Euromed.AOE.menu.Replay

mainClock = pygame.time.Clock()
from pygame.locals import *

pygame.init()
pygame.display.set_caption('Age of Euromed Empire')
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
font = pygame.font.SysFont(None, 80)
image = pygame.image.load("greek-wars-mosaic.jpg").convert_alpha()
image2 = pygame.transform.scale(image, (screen.get_width(), screen.get_height()))


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

    click = False


class Match:
    def __init__(self):
        pygame.display.update()
        running = True

        while running:

            screen.fill((0, 0, 0))
            screen.blit(image2, (0, 0))
            mx, my = pygame.mouse.get_pos()
            draw_text('MATCH', font, (0,0,0), screen, screen.get_width() / 2, screen.get_height() / 6.5)

            Euromed.AOE.menu.Bibliotheque.button("Retour", screen.get_width()*(5/6), screen.get_height()*(5/6),screen.get_width() / 7, screen.get_height() / 10, (0, 200, 250), (255, 0, 255), Euromed.AOE.menu.Menu_principal.Menu)
            Euromed.AOE.menu.Bibliotheque.button("Nouveau Match", 255, 255, screen.get_width() / 4,
                                screen.get_height() / 8, (0,0,0), (35,35,35),
                                Euromed.AOE.menu.Nouveau_match.Nouveau)

            Euromed.AOE.menu.Bibliotheque.button("Reprendre partie", screen.get_width()/2, screen.get_height()*(2.25/4), screen.get_width() / 4,
                                screen.get_height() / 8, (0,0,0), (35,35,35),
                                Euromed.AOE.menu.Reprendre_match.Reprise)
            #Bibliotheque.button("test", 425, 425, 50, 50, (0, 255, 250), (255, 0, 255), Test3.Matchtest)


            click = False
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

            pygame.display.update()
            mainClock.tick(60)
