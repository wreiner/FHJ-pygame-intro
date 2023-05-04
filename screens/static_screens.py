import pygame
from screens.defaults import *

def welcome_screen(screen, msg):
    font = None

    # use sourcecodepro if possbel
    if "sourcecodepro" in pygame.font.get_fonts():
        font = pygame.font.SysFont("sourcecodepro", 36)

    txtsurf = font.render(msg, True, COLOR_RED)
    screen.blit(txtsurf,(WINDOW_WIDTH/2 - txtsurf.get_width() // 2, WINDOW_HEIGHT/2 - txtsurf.get_height() // 2))

def other_screen(screen, msg):
    font = None

    # use sourcecodepro if possbel
    if "sourcecodepro" in pygame.font.get_fonts():
        font = pygame.font.SysFont("sourcecodepro", 36)

    txtsurf = font.render(msg, True, COLOR_BLUE)
    screen.blit(txtsurf,(WINDOW_WIDTH/2 - txtsurf.get_width() // 2, WINDOW_HEIGHT/2 - txtsurf.get_height() // 2))
