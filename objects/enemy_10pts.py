import random
import pygame
from screens.defaults import *
from objects.laser import Laser


class Enemy10Pts(pygame.sprite.Sprite):
    def __init__(self, picture_path, screen):
        super().__init__()
        self.screen = screen

        self.image = pygame.image.load(picture_path)
        self.image = pygame.transform.scale(self.image, (50, 50))

        # get the current location of the player
        self.rect = self.image.get_rect()
        self.width = self.rect.width
        self.height = self.rect.height
        self.y_coord = 65

        self.hit = False
        self.score_points = 10

        self.laser_obj = Laser(self.screen, COLOR_RED, "enemy")

    def set_x(self, x_coord):
        # keep the player character within the bounds of the screen
        if x_coord < 0:
            x_coord = 0
        elif x_coord + self.image.get_width() > WINDOW_WIDTH:
            x_coord = WINDOW_WIDTH - self.image.get_width()

        self.x_coord = x_coord

    def update_x(self, x_upd):
        y2update = False
        x_coord = self.x_coord

        x_coord += x_upd

        # if enemy hits screen wall
        if x_coord < 0:
            x_coord = 0
            y2update = True
        elif x_coord + self.image.get_width() > WINDOW_WIDTH:
            x_coord = WINDOW_WIDTH - self.image.get_width()
            y2update = True

        self.x_coord = x_coord

        # if self.laser_obj.draw_laser == False and ((random.randint(0, 100) * random.randint(0, 1000)) % 73) == 0:
        #     self.laser_obj.update_coords(self.x_coord + self.width/2 - 1, self.y_coord + self.height + 5)
        #     self.laser_obj.draw_laser = True

        return y2update

    def fire(self):
        self.laser_obj.update_coords(self.x_coord + self.width/2 - 1, self.y_coord + self.height + 5)
        self.laser_obj.draw_laser = True

    def set_hit(self):
        self.hit = True

    def update_y(self, y_upd):
        y_coord = self.y_coord

        y_coord += y_upd
        self.y_coord = y_coord

    def draw(self):
        if not self.hit:
            self.screen.blit(self.image, (self.x_coord, self.y_coord))
