import Euromed.AOE.AOE.main
import main
from Euromed.AOE.menu.Menu_principal import *
mainClock = pygame.time.Clock()
from pygame.locals import *
import Euromed.AOE.menu.Match
import Euromed.AOE.menu.Menu_principal
import Euromed.AOE.menu.Bibliotheque
import Euromed.AOE.menu.Match


pygame.init()
pygame.display.set_caption('Age of Euromed Empire')
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
font = pygame.font.SysFont(None, 20)
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

    click = False




def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

    click = False


class Nouveau:

    def __init__(self):
        running = True
        while running:
            screen.fill((0, 0, 0))
            mx, my = pygame.mouse.get_pos()
            draw_text('Nouveau match', font, (0, 0, 0), screen, 250, 50)
            draw_text('NOUVEAU MATCH', font, (255, 255, 255), screen, 20, 20)

            Euromed.AOE.menu.Bibliotheque.button("Retour", 425, 425, 50, 50, (0, 255, 250), (255, 0, 255), Euromed.AOE.menu.Match.Match)
            Euromed.AOE.menu.Bibliotheque.button("go go", 425, 200, 50, 50, (0, 255, 250), (255, 0, 255), Euromed.AOE.AOE.main.main())
            #menu.Bibliotheque.lets_go_button("Let's go", 425, 200, 50, 50, (0, 255, 250), (255, 0, 255))

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



