from Menu_principal import *

class Game:

    def game():
        running = True
        while running:
            screen.fill((0, 0, 0))

            draw_text('GAME', font, (255, 255, 255), screen, 20, 20)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

            pygame.display.update()
mainClock.tick(60)