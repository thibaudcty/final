""""#!/usr/bin/python3.4
# Setup Python ----------------------------------------------- #
import pygame, sys

# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *

pygame.init()
pygame.display.set_caption('game base')
screen = pygame.display.set_mode((500, 500), 0, 32)

font = pygame.font.SysFont(None, 20)


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


click = False


def main_menu():
    while True:

        screen.fill((240, 220, 255))
        draw_text('main menu', font, (255, 255, 255), screen, 20, 20)
        draw_text('MENU', font, (0, 0, 0), screen, 250, 50)
        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(30, 100, 200, 50)
        if button_1.collidepoint((mx, my)):
            if click:
                test.options_5()
        pygame.draw.rect(screen, (255, 0, 0), button_1)

        button_2 = pygame.Rect(50, 200, 200, 50)
        if button_2.collidepoint((mx, my)):
            if click:
                options()
        pygame.draw.rect(screen, (255, 0, 0), button_2)

        button_3 = pygame.Rect(70, 300, 200, 50)
        if button_3.collidepoint((mx, my)):
            if click:
                game()
        pygame.draw.rect(screen, (255, 0, 250), button_3)

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


def options():
    running = True
    while running:
        screen.fill((0, 0, 0))
        mx, my = pygame.mouse.get_pos()
        draw_text('options', font, (0, 0, 0), screen, 250, 50)
        draw_text('options', font, (255, 255, 255), screen, 20, 20)

        button_4 = pygame.Rect(70, 300, 200, 50)
        if button_4.collidepoint((mx, my)):
            if click:
                options_3()
        pygame.draw.rect(screen, (255, 0, 250), button_4)

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


def options_2():
    running = True
    while running:
        screen.fill((150, 0, 0))

        draw_text('options_2', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)


def options_3():
    running = True
    while running:
        screen.fill((0, 0, 150))

        draw_text('options_3', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)


main_menu()
"""