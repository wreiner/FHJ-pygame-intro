import pygame

def show_fonts():
    fonts = pygame.font.get_fonts()
    for f in fonts:
        print(f)
    pygame.quit()
