import pygame
from screens.defaults import *
from objects.laser import Laser


class PlayerShip(pygame.sprite.Sprite):
    def __init__(self, picture_path, screen):
        super().__init__()
        self.screen = screen

        self.image = pygame.image.load(picture_path)
        self.image = pygame.transform.scale(self.image, (50, 50))

        # get the current location of the player
        self.rect = self.image.get_rect()

        self.width = self.rect.width

        self.x_coord = 0
        self.y_coord = WINDOW_HEIGHT - 65

        self.laser_obj = Laser(self.screen, COLOR_GREEN, "player")

    def set_x(self, x_coord):
        # keep the player character within the bounds of the screen
        if x_coord < 0:
            x_coord = 0
        elif x_coord + self.image.get_width() > WINDOW_WIDTH:
            x_coord = WINDOW_WIDTH - self.image.get_width()

        self.x_coord = x_coord

    def draw(self):
        self.screen.blit(self.image, (self.x_coord, self.y_coord))
