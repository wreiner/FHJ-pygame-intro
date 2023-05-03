import pygame
from screens.defaults import *


class Bunker:
    def __init__(self, screen, start_x_coord, start_y_coord):
        self.screen = screen

        self.poly_multiplier = 10
        self.points = [
            ((2 * self.poly_multiplier) + start_x_coord, (0 * self.poly_multiplier) + start_y_coord),
            ((6 * self.poly_multiplier) + start_x_coord, (0 * self.poly_multiplier) + start_y_coord),
            ((8 * self.poly_multiplier) + start_x_coord, (2 * self.poly_multiplier) + start_y_coord),
            ((8 * self.poly_multiplier) + start_x_coord, (5 * self.poly_multiplier) + start_y_coord),
            ((6 * self.poly_multiplier) + start_x_coord, (5 * self.poly_multiplier) + start_y_coord),
            ((6 * self.poly_multiplier) + start_x_coord, (3 * self.poly_multiplier) + start_y_coord),
            ((5 * self.poly_multiplier) + start_x_coord, (2 * self.poly_multiplier) + start_y_coord),
            ((3 * self.poly_multiplier) + start_x_coord, (2 * self.poly_multiplier) + start_y_coord),
            ((2 * self.poly_multiplier) + start_x_coord, (3 * self.poly_multiplier) + start_y_coord),
            ((2 * self.poly_multiplier) + start_x_coord, (5 * self.poly_multiplier) + start_y_coord),
            ((0 * self.poly_multiplier) + start_x_coord, (5 * self.poly_multiplier) + start_y_coord),
            ((0 * self.poly_multiplier) + start_x_coord, (2 * self.poly_multiplier) + start_y_coord),
            ((2 * self.poly_multiplier) + start_x_coord, (0 * self.poly_multiplier) + start_y_coord)
        ]
        self.color = COLOR_GREEN

        self.width = (8 * self.poly_multiplier) + start_x_coord

    def get_width(self):
        return self.width

    def __UDinit__(self, screen, start_x_coord, start_y_coord):
        self.screen = screen

        self.poly_multiplier = 10
        self.points = [
            ((1 * self.poly_multiplier) + start_x_coord, (0 * self.poly_multiplier) + start_y_coord),
            ((1 * self.poly_multiplier) + start_x_coord, (3 * self.poly_multiplier) + start_y_coord),
            ((3 * self.poly_multiplier) + start_x_coord, (5 * self.poly_multiplier) + start_y_coord),
            ((7 * self.poly_multiplier) + start_x_coord, (5 * self.poly_multiplier) + start_y_coord),
            ((9 * self.poly_multiplier) + start_x_coord, (3 * self.poly_multiplier) + start_y_coord),
            ((9 * self.poly_multiplier) + start_x_coord, (0 * self.poly_multiplier) + start_y_coord),
            ((7 * self.poly_multiplier) + start_x_coord, (0 * self.poly_multiplier) + start_y_coord),
            ((7 * self.poly_multiplier) + start_x_coord, (2 * self.poly_multiplier) + start_y_coord),
            ((6 * self.poly_multiplier) + start_x_coord, (3 * self.poly_multiplier) + start_y_coord),
            ((4 * self.poly_multiplier) + start_x_coord, (3 * self.poly_multiplier) + start_y_coord),
            ((3 * self.poly_multiplier) + start_x_coord, (2 * self.poly_multiplier) + start_y_coord),
            ((3 * self.poly_multiplier) + start_x_coord, (0 * self.poly_multiplier) + start_y_coord),
            ((1 * self.poly_multiplier) + start_x_coord, (0 * self.poly_multiplier) + start_y_coord)
        ]
        self.color = COLOR_GREEN

    def draw(self) :
        pygame.draw.polygon(self.screen, self.color, self.points)
