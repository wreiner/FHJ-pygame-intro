#!/usr/bin/env python3

import pygame
import random

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
    background_img = pygame.image.load(BACKGROUNG_IMG)
    background_img = pygame.transform.scale(background_img, (WINDOW_WIDTH, WINDOW_HEIGHT))

    player = PlayerShip(PLAYER_SHIP, SCREEN)
    # sprites = pygame.sprite.Group(player)

    enemies = []
    # enemies.clear()

    score = 0
    lives = 3

    for i in range(0, 11):
        enemy10pts = Enemy10Pts(ENEMY_10PTS, SCREEN)
        enemy10pts.set_x(10 + 55 * i)

        enemies.append(enemy10pts)

        # sprites = pygame.sprite.Group(player)

    player_speed = 0
    player_x = 0
    enemy_speed = ENEMY_X_STEPS
    enemy_speed_inv = 1

    update_y = False

    timer = random.uniform(2, 6)
    dt = 0
    running = True

    while running:
        # DEBUG SCREENS
        # font_screen("SCORE LIVES 1234567890")
        # show_fonts()

        # Decrease the timer by the delta time.
        timer -= dt

        SCREEN.fill((0, 0, 0))
        SCREEN.blit(background_img, (0, 0))

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
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_LEFT, pygame.K_a):
                    player_speed = PLAYER_X_STEPS * -1

                if event.key in (pygame.K_RIGHT, pygame.K_d):
                    player_speed = PLAYER_X_STEPS

                if event.key == pygame.K_SPACE:
                    if not player.laser_obj.draw_laser:
                        player.laser_obj.update_coords(player.x_coord + player.width/2 - 1, player.y_coord - 50)
                        player.laser_obj.draw_laser = True

            if event.type == pygame.KEYUP:
                if event.key in (pygame.K_LEFT, pygame.K_a, pygame.K_RIGHT, pygame.K_d):
                    player_speed = 0

        player_x += player_speed
        player.set_x(player_x)

        if timer <= 0:
            # Pick a random enemy to get the x and y coords.
            random_enemy = random.choice(enemies)
            if not random_enemy.hit:
                # enemy_x, enemy_y = random_enemy.rect.center
                # bullet = BulletEnemy(enemy_x, enemy_y)
                random_enemy.fire()
                timer = random.uniform(2, 6)  # Reset the timer.

        for enemy in enemies:
            if enemy.update_x(enemy_speed * enemy_speed_inv) or update_y:
                enemy_speed_inv *= -1
                update_y = True
            if enemy.laser_obj.draw_laser:
                enemy.laser_obj.update_y_coord(LASER_Y_STEPS)

        if update_y:
            for enemy in enemies:
                enemy.update_y(ENEMY_Y_STEPS)

                if enemy == enemies[-1]:
                    update_y = False

        if player.laser_obj.draw_laser:
            player.laser_obj.update_y_coord(LASER_Y_STEPS)

        # collission detection
        for enemy in enemies:
            if player.laser_obj.check_collision(enemy.x_coord, enemy.y_coord + enemy.height, enemy.x_coord + enemy.width):
                enemy.set_hit()
                player.laser_obj.reset_laser()

            if enemy.laser_obj.check_collision(player.x_coord, player.y_coord, player.x_coord + player.width):
                # player hit
                print(f"player has been hit {lives}")
                enemy.laser_obj.reset_laser()
                lives -= 1

        if lives == 0:
            print("GAME OVER")
            running = False

        # redraw screen
        game_screen(230, 3, SCREEN)
        for enemy in enemies:
            enemy.draw()
            if enemy.laser_obj.draw_laser:
                enemy.laser_obj.draw()
        player.draw()
        if player.laser_obj.draw_laser:
            player.laser_obj.draw()

        pygame.display.update()

        dt = CLOCK.tick(60) / 400  # / 1000 to convert it to seconds.

    pygame.quit()

if __name__=="__main__":
    main()
