import pygame
from screens.defaults import *


class PlayerShip(pygame.sprite.Sprite):
    def lala(self):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.image = pygame.transform.scale(self.image, (50, 50))

        # get the current location of the player
        self.player_loc = self.image.get_rect()

        # self.image = pygame.Surface([width, height])
        # self.image.fill(SURFACE_COLOR)
        # self.image.set_colorkey(COLOR)

        # pygame.draw.rect(self.image,
        #                  color,
        #                  pygame.Rect(0, 0, width, height))

        # Display the player sprite at x
        # and y coordinates
        self.screen = screen

        self.screen.blit(self.image, (WINDOW_WIDTH - 65, WINDOW_HEIGHT - 65))

    def __init__(self, picture_path, screen):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.image = pygame.transform.scale(self.image, (50, 50))

        # get the current location of the player
        self.rect = self.image.get_rect()

        # self.image = pygame.Surface([width, height])
        # self.image.fill(SURFACE_COLOR)
        # self.image.set_colorkey(COLOR)

        # pygame.draw.rect(self.image,
        #                  color,
        #                  pygame.Rect(0, 0, width, height))

        # Display the player sprite at x
        # and y coordinates
        self.screen = screen
        self.screen.blit(self.image, (WINDOW_WIDTH - 65, WINDOW_HEIGHT - 65))

    def set_x(self, x_coord):
        # keep the player character within the bounds of the screen
        if x_coord < 0:
            x_coord = 0
        elif x_coord + self.image.get_width() > WINDOW_WIDTH:
            x_coord = WINDOW_WIDTH - self.image.get_width()
        self.screen.blit(self.image, (x_coord, WINDOW_HEIGHT - 65))


    def moveRight(self, pixels):
        self.rect.x += pixels

    def moveLeft(self, pixels):
        self.rect.x -= pixels
