import pygame


WIDTH, HEIGHT = 1300, 800
GREEN = (0,255,0)
BLACK = (20,20,20)
WHITE = (255,255,255)
TILE_SIZE = 40 #edit block size
MAP_SIZE = 80
LES_RESSOURCES = {"WOOD","STONE"}
NB_ARBRES = 25
FPS =60
def lerp(a,b,t):
    return a*(1-t) + b*t

def draw_text(screen, text, size, colour, pos):

    font = pygame.font.SysFont(None, size)
    text_surface = font.render(text, True, colour)
    text_rect = text_surface.get_rect(topleft=pos)
    screen.blit(text_surface, text_rect)
