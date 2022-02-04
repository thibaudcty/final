from Euromed.AOE.menu import Menu_principal
from Euromed.AOE.menu.Menu_principal import *
mainClock = pygame.time.Clock()
from pygame.locals import *
import Euromed.AOE.menu.Bibliotheque
import Euromed.AOE.menu.Menu_principal
pygame.init()
pygame.display.set_caption('Age of Euromed Empire')
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
font = pygame.font.SysFont(None, 80)
image = pygame.image.load("image3.jpg").convert_alpha()
image2 = pygame.transform.scale(image, (screen.get_width(), screen.get_height()))

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

    click = False

class Replay_function:
    def __init__(self):
        running = True
        while running:
            screen.blit(image2, (0,0))
            draw_text('REPLAY', font, (0,0,0), screen, screen.get_width() / 2, screen.get_height() / 6.5)

            mx, my = pygame.mouse.get_pos()

            Euromed.AOE.menu.Bibliotheque.button("Retour", screen.get_width() * (5 / 6), screen.get_height() * (5 / 6),
                                     screen.get_width() / 7, screen.get_height() / 10, (0, 200, 250), (255, 0, 255),
                                     Euromed.AOE.menu.Menu_principal.Menu)


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
