import Euromed.AOE.menu.Replay
import Euromed.AOE.menu.Test
import Euromed.AOE.menu.Test2
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
screen = pygame.display.set_mode((500, 500), 0, 32)
font = pygame.font.SysFont(None, 20)
image = pygame.image.load("gaulois.jpg").convert_alpha()
image2 = pygame.transform.scale(image, (500, 500))


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

    click = False


class Matchtest:
    def __init__(self):
        pygame.display.update()
        running = True

        while running:

            screen.fill((0, 0, 0))
            screen.blit(image2, (0, 0))
            mx, my = pygame.mouse.get_pos()
            draw_text('Match', font, (0, 0, 0), screen, 250, 50)
            draw_text('MATCH', font, (255, 255, 255), screen, 20, 20)

            Euromed.AOE.menu.Bibliotheque.button("Retour", 100, 425, 50, 50, (0, 255, 250), (255, 0, 255), Euromed.AOE.menu.Menu_principal.Menu)
            Euromed.AOE.menu.Bibliotheque.button("Nouveau Match", 100, 200, 100, 50, (255, 0, 150), (255, 0, 255),
                                Euromed.AOE.menu.Nouveau_match.Nouveau)

            Euromed.AOE.menu.Bibliotheque.button("Reprendre partie", 100, 300, 100, 50, (255, 0, 150), (255, 0, 255),
                                Euromed.AOE.menu.Reprendre_match.Reprise)
            Euromed.AOE.menu.Bibliotheque.button("test", 425, 425, 50, 50, (0, 255, 250), (255, 0, 255), Euromed.AOE.menu.Test2.Test2)


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
