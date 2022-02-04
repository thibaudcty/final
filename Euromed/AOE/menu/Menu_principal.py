import pygame, sys

import Euromed.AOE.menu.Bibliotheque
import Euromed.AOE.menu.Match
import Euromed.AOE.menu.Parametres
import Euromed.AOE.menu.Replay

mainClock = pygame.time.Clock()
from pygame.locals import *

pygame.init()
pygame.display.set_caption('Age of Euromed Empire')
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
font = pygame.font.SysFont(None, 80)
font2=pygame.font.SysFont(None, 120)


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)


image = pygame.image.load("image_menu.jpg").convert_alpha()
image2 = pygame.transform.scale(image, (screen.get_width(), screen.get_height()))
mouse = pygame.mouse.get_pos()
click = pygame.mouse.get_pressed()


class Menu:

    def __init__(self):

        while True:
            screen.fill((0, 0, 0))

            screen.blit(image2, (0, 0))
            draw_text('AGE OF EUROMED EMPIRE', font2, (255, 255, 255), screen, screen.get_width() / 2, screen.get_height() / 6)
            draw_text('MENU PRINCIPAL', font, (255, 255, 255), screen, screen.get_width() / 2, screen.get_height() / 4)
            mx, my = pygame.mouse.get_pos()

            Euromed.AOE.menu.Bibliotheque.button("Match", screen.get_width() / 2, screen.get_height() / 2.3, screen.get_width() / 6,
                                     screen.get_height() / 10, (0, 0, 0), (30, 30, 30),
                                     Euromed.AOE.menu.Match.Match)

            Euromed.AOE.menu.Bibliotheque.button("Parametres", screen.get_width() / 2, screen.get_height() / 1.7,
                                     screen.get_width() / 6,
                                     screen.get_height() / 10, (0, 0, 0), (30, 30, 30),
                                     Euromed.AOE.menu.Parametres.Para)

            Euromed.AOE.menu.Bibliotheque.button("Replay", screen.get_width() / 2, screen.get_height() / 1.35,
                                     screen.get_width() / 6,
                                     screen.get_height() / 10, (0, 0, 0), (30, 30, 30),
                                     Euromed.AOE.menu.Replay.Replay_function)

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
