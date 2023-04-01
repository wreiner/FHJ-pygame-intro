#!/usr/bin/env python3

import pygame

from objects.bunker import Bunker
from objects.player_ship import PlayerShip

from screens.defaults import *
from screens.dynamic_screens import game_screen
from screens.static_screens import other_screen, welcome_screen


def main():
    global SCREEN, CLOCK

    # FIXME set to false after testin
    splash_shown = True

    pygame.init()

    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption(WINDOW_TITLE)
    CLOCK = pygame.time.Clock()

    player = PlayerShip(PLAYER_SHIP, SCREEN)
    sprites = pygame.sprite.Group(player)

    while True:
        # DEBUG SCREENS
        # font_screen("SCORE LIVES 1234567890")
        # show_fonts()

        game_screen(230, 3, SCREEN)

        if splash_shown == False:
                print("in splash check")
                welcome_screen("welcome_screen")
                pygame.display.update()
                pygame.time.wait(3000)
                splash_shown = True
                SCREEN.fill(COLOR_WHITE)
                other_screen("main screen?")

        for event in pygame.event.get():

            # print(f"got event: {event} ..")
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_LEFT, pygame.K_a):
                    player.moveLeft(5)

                if event.key in (pygame.K_RIGHT, pygame.K_d):
                    player.moveRight(5)

        sprites.update(SCREEN)
        sprites.draw(SCREEN)
        pygame.display.update()

if __name__=="__main__":
    main()
