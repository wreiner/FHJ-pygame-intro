import pygame
from screens.defaults import *


class Enemy10Pts(pygame.sprite.Sprite):
    def __init__(self, picture_path, screen):
        super().__init__()
        self.screen = screen

        self.image = pygame.image.load(picture_path)
        self.image = pygame.transform.scale(self.image, (50, 50))

        # get the current location of the player
        self.rect = self.image.get_rect()
        self.y_coord = 65

    def set_x(self, x_coord):
        # keep the player character within the bounds of the screen
        if x_coord < 0:
            x_coord = 0
        elif x_coord + self.image.get_width() > WINDOW_WIDTH:
            x_coord = WINDOW_WIDTH - self.image.get_width()
        self.screen.blit(self.image, (x_coord, 65))
        self.x_coord = x_coord

    def update_x(self, x_upd):
        y2update = False
        x_coord = self.x_coord

        x_coord += x_upd

        # keep the player character within the bounds of the screen
        if x_coord < 0:
            x_coord = 0
            y2update = True
        elif x_coord + self.image.get_width() > WINDOW_WIDTH:
            x_coord = WINDOW_WIDTH - self.image.get_width()
            y2update = True
        self.screen.blit(self.image, (x_coord, self.y_coord))

        self.x_coord = x_coord

        return y2update

    def update_y(self, y_upd):
        y_coord = self.y_coord

        y_coord += y_upd
        self.y_coord = y_coord

        self.screen.blit(self.image, (self.x_coord, self.y_coord))
