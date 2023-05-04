import pygame
import time
from screens.defaults import *


class Laser:
    def __init__(self, screen, laser_color, parent_type):
        self.screen = screen
        self.color = laser_color
        self.create_laser_rect()
        self.draw_laser = False

        self.x_coord = -1
        self.y_coord = -1

        self.laser_direction = 1

        if parent_type == "player":
            self.laser_direction *= -1

    def create_laser_rect(self):
        # surface = pygame.display.set_mode((400, 300))
        # self.laser = pygame.draw.rect(surface, self.color, pygame.Rect(30, 30, 60, 60))
        self.laser = pygame.rect.Rect((64, 54, 16, 16))
        self.width = self.laser.width

    def update_coords(self, parent_x_coord, parent_y_coord):
        self.x_coord = parent_x_coord
        self.y_coord = parent_y_coord
        self.laser = pygame.rect.Rect((parent_x_coord, parent_y_coord, 2, 5))

    def update_y_coord(self, y_coord):
        self.y_coord += y_coord * self.laser_direction
        self.laser = pygame.rect.Rect((self.x_coord, self.y_coord, 2, 5))

        if self.laser_direction > 0 and self.y_coord > WINDOW_HEIGHT:
                self.draw_laser = False
        if self.laser_direction < 0 and self.y_coord < 0:
                self.draw_laser = False

    def check_collision(self, target_left_x_coord, target_left_y_coord, target_right_x_coord):
        print(f"LASER({self.x_coord}/{self.y_coord})")
        # print(f"ENEMY({target_left_x_coord} - {target_right_x_coord}/{target_left_y_coord})")

        if self.x_coord >= target_left_x_coord and self.x_coord + self.width <= target_right_x_coord and self.y_coord <= target_left_y_coord:
            return True
        return False

    def reset_laser(self):
        self.draw_laser = False
        self.x_coord = -1
        self.y_coord = -1

    def draw(self):
        if self.draw_laser:
            pygame.draw.rect(self.screen, self.color, self.laser)
