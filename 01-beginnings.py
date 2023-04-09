#!/usr/bin/env python3

import pygame

from objects.bunker import Bunker
from objects.player_ship import PlayerShip
from objects.enemy_10pts import Enemy10Pts

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
    # sprites = pygame.sprite.Group(player)

    enemies = []
    # enemies.clear()

    for i in range(0, 11):
        enemy10pts = Enemy10Pts(ENEMY_10PTS, SCREEN)
        enemy10pts.set_x(10 + 50*i)

        enemies.append(enemy10pts)

        # sprites = pygame.sprite.Group(player)

    player_speed = 0
    player_x = 0
    enemy_speed = ENEMY_X_STEPS
    enemy_speed_inv = 1

    update_y = False

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
                    player_speed = -1

                if event.key in (pygame.K_RIGHT, pygame.K_d):
                    player_speed = 1

            if event.type == pygame.KEYUP:
                if event.key in (pygame.K_LEFT, pygame.K_a, pygame.K_RIGHT, pygame.K_d):
                    player_speed = 0

        player_x += player_speed

        for enemy in enemies:
            if enemy.update_x(enemy_speed * enemy_speed_inv) or update_y:
                enemy_speed_inv *= -1
                update_y = True

        if update_y:
            for enemy in enemies:
                enemy.update_y(ENEMY_Y_STEPS)

            if enemy == enemies[-1]:
                update_y = False

        player.set_x(player_x)
        pygame.display.update()


if __name__=="__main__":
    main()
