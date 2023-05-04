import pygame
from screens.defaults import *
from objects.bunker import Bunker


def game_screen(score, lives, screen):
    font_name = "fonts/ComputerPixel7-mnL2.ttf"
    size = 30
    font = pygame.font.Font(font_name, size)
    txtsurf = font.render(f"SCORE: {score}", True, COLOR_BLACK)
    screen.blit(txtsurf,(10, 10))

    txtsurf = font.render(f"LIVES: {lives}", True, COLOR_WHITE)
    screen.blit(txtsurf,(WINDOW_WIDTH - txtsurf.get_width() - 10, 10))

    bunker_left = Bunker(screen, 70, WINDOW_HEIGHT - 150)
    bunker_left.draw()

    bunker_middle = Bunker(screen, bunker_left.get_width() + 120, WINDOW_HEIGHT - 150)
    bunker_middle.draw()

    bunker_right = Bunker(screen, bunker_middle.get_width() + 120, WINDOW_HEIGHT - 150)
    bunker_right.draw()

    # poly_multiplier = 10

    # pygame.draw.polygon(screen, COLOR_GREEN, (
    #         (1 * poly_multiplier, 0 * poly_multiplier),
    #         (1 * poly_multiplier, 3 * poly_multiplier),
    #         (3 * poly_multiplier, 5 * poly_multiplier),
    #         (7 * poly_multiplier, 5 * poly_multiplier),
    #         (9 * poly_multiplier, 3 * poly_multiplier),
    #         (9 * poly_multiplier, 0 * poly_multiplier),
    #         (7 * poly_multiplier, 0 * poly_multiplier),
    #         (7 * poly_multiplier, 2 * poly_multiplier),
    #         (6 * poly_multiplier, 3 * poly_multiplier),
    #         (4 * poly_multiplier, 3 * poly_multiplier),
    #         (3 * poly_multiplier, 2 * poly_multiplier),
    #         (3 * poly_multiplier, 0 * poly_multiplier),
    #         (1 * poly_multiplier, 0 * poly_multiplier)
    #     ))