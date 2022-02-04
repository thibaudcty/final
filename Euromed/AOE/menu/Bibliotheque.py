import Euromed.AOE.menu.Match
import Euromed.AOE.menu.Menu_principal
from Euromed.AOE.menu.Menu_principal import *

mainClock = pygame.time.Clock()
from pygame.locals import *

pygame.init()
pygame.display.set_caption('Age of Euromed Empire')
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
font = pygame.font.SysFont(None, 20)






def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


black = (255, 255, 255)


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def button(msg, x, y, w, h, ic, ac, action):
    x = x - (w / 2)
    y = y - (h / 2)

    mouse = pygame.mouse.get_pos()

    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, ac, (x, y, w, h))

        if click[0] == 1:
            print("il a cliqué !!!")

            action()

    else:
        pygame.draw.rect(screen, ic, (x, y, w, h))

    seize = screen.get_width() / 40
    seize = int(seize)

    smallText = pygame.font.SysFont("comicsansms", seize)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    screen.blit(textSurf, textRect)
    click = False




class Biblio:

    def boutton_retour(click, mx, my):
        button_retour = pygame.Rect(30, 100, 200, 50)
        if button_retour.collidepoint((mx, my)):
            if click:
                Euromed.AOE.menu.Menu_principal.Menu()
        pygame.draw.rect(screen, (255, 0, 0), button_retour)
