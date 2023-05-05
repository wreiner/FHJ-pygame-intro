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
    # initialize pygame
    pygame.init()
    running = True

    # FIXME set to false after testin
    splash_shown = True

    # -- setup the window
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    background_img = pygame.image.load(BACKGROUNG_IMG)
    background_img = pygame.transform.scale(background_img, (WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption(WINDOW_TITLE)

    # -- setup the clock
    CLOCK = pygame.time.Clock()

    # -- setup the player
    player = PlayerShip(PLAYER_SHIP, SCREEN)
    player_speed = 0
    player_x = 0

    score = 0
    lives = 3

    # -- setup enemies
    enemies = []
    enemy_speed = ENEMY_X_STEPS
    enemy_speed_inv = 1

    # used to propagate y movement of enemies
    update_y = False

    # randomize enemy shooting
    timer = random.uniform(2, 6)
    dt = 0

    # a row has 11 enemies
    for i in range(0, 11):
        enemy10pts = Enemy10Pts(ENEMY_10PTS, SCREEN)
        enemy10pts.set_x(10 + 55 * i)

        enemies.append(enemy10pts)

    enemies_nothit = len(enemies)

    # MAIN GAME LOOP
    while running:
        # build the base of the screen as it should be at the back
        SCREEN.fill((0, 0, 0))
        SCREEN.blit(background_img, (0, 0))

        # Decrease the timer by the delta time.
        timer -= dt

        # show splash screen
        if splash_shown == False:
                print("in splash check")
                welcome_screen(SCREEN, "SPACE INVADERS")
                pygame.display.update()
                pygame.time.wait(3000)
                splash_shown = True
                continue

        # handle user inputs
        for event in pygame.event.get():
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

        # it is random time to try to shoot the player
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

        # propagate y movement of all enemies
        if update_y:
            for enemy in enemies:
                enemy.update_y(ENEMY_Y_STEPS)

                if enemy == enemies[-1]:
                    update_y = False

        # draw the player laser
        if player.laser_obj.draw_laser:
            player.laser_obj.update_y_coord(LASER_Y_STEPS)

        # collission detection
        for enemy in enemies:
            # check if player hit any enemy
            if not enemy.hit and player.laser_obj.check_collision(enemy.x_coord, enemy.y_coord + enemy.height, enemy.x_coord + enemy.width):
                enemy.set_hit()
                score += enemy.score_points
                enemies_nothit -= 1
                player.laser_obj.reset_laser()
                print(f"enemy has ben hit {enemies_nothit}")

            # check if an enemy hit the player
            if enemy.laser_obj.check_collision(player.x_coord, player.y_coord, player.x_coord + player.width):
                # player hit
                print(f"player has been hit {lives}")
                enemy.laser_obj.reset_laser()
                lives -= 1

        # other game states
        if lives == 0:
            print("GAME OVER")
            running = False

        if enemies_nothit == 0:
            print("YOU WON")
            running = False

        # redraw screen
        game_screen(score, lives, SCREEN)
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
