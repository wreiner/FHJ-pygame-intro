#!/usr/bin/env python3

import pygame

WINDOW_HEIGHT = 800
WINDOW_WIDTH = 600

COLOR_WHITE = (255,255,255)
COLOR_RED = (255,0,0)
COLOR_GREEN = (0,255,0)
COLOR_BLUE = (0,0,255)


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

def welcome_screen(msg):
    font = None

    # use sourcecodepro if possbel
    if "sourcecodepro" in pygame.font.get_fonts():
        font = pygame.font.SysFont("sourcecodepro", 36)

    txtsurf = font.render(msg, True, COLOR_RED)
    SCREEN.blit(txtsurf,(WINDOW_WIDTH/2 - txtsurf.get_width() // 2, WINDOW_HEIGHT/2 - txtsurf.get_height() // 2))

def other_screen(msg):
    font = None

    # use sourcecodepro if possbel
    if "sourcecodepro" in pygame.font.get_fonts():
        font = pygame.font.SysFont("sourcecodepro", 36)

    txtsurf = font.render(msg, True, COLOR_BLUE)
    SCREEN.blit(txtsurf,(WINDOW_WIDTH/2 - txtsurf.get_width() // 2, WINDOW_HEIGHT/2 - txtsurf.get_height() // 2))

def game_screen(score, lives):
    font_name = "fonts/ComputerPixel7-mnL2.ttf"
    size = 30
    font = pygame.font.Font(font_name, size)
    txtsurf = font.render(f"SCORE: {score}", True, COLOR_WHITE)
    SCREEN.blit(txtsurf,(10, 10))

    txtsurf = font.render(f"LIVES: {lives}", True, COLOR_WHITE)
    SCREEN.blit(txtsurf,(WINDOW_WIDTH - txtsurf.get_width() - 10, 10))

    bunker_left = Bunker(SCREEN, 70, WINDOW_HEIGHT - 150)
    bunker_left.draw()

    bunker_middle = Bunker(SCREEN, bunker_left.get_width() + 120, WINDOW_HEIGHT - 150)
    bunker_middle.draw()

    bunker_right = Bunker(SCREEN, bunker_middle.get_width() + 120, WINDOW_HEIGHT - 150)
    bunker_right.draw()

    # poly_multiplier = 10

    # pygame.draw.polygon(SCREEN, COLOR_GREEN, (
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

def font_screen(msg):
    font = None

    # use sourcecodepro if possbel
    fonts = pygame.font.get_fonts()
    h = 20
    size = 20
    # for f in fonts:
    #     font = pygame.font.SysFont(f, size)
    #     txtsurf = font.render(msg, True, COLOR_GREEN)
    #     SCREEN.blit(txtsurf,(10, h))
    #     h += size * 1.5

    for f in ["ComputerPixel7-mnL2.ttf", "ConnectionIi-2wj8.otf", "ComputerPixel7-mnL2.ttf", "PixeloidMono-VGj6x.ttf", "PixeloidSansBold-GOjpP.ttf", "PixeloidSans-JR6qo.ttf"]:
        font = pygame.font.Font("fonts/" + f, size)
        txtsurf = font.render(msg, True, COLOR_GREEN)
        SCREEN.blit(txtsurf,(10, h))
        h += size * 1.5

def show_fonts():
    fonts = pygame.font.get_fonts()
    for f in fonts:
        print(f)
    pygame.quit()

def main():
    global SCREEN, CLOCK

    # FIXME set to false after testin
    splash_shown = True

    pygame.init()

    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()

    while True:
        # font_screen("SCORE LIVES 1234567890")
        game_screen(230, 3)
        # show_fonts()
        if splash_shown == False:
                print("in splash check")
                welcome_screen("welcome_screen")
                pygame.display.update()
                pygame.time.wait(3000)
                splash_shown = True
                SCREEN.fill(COLOR_WHITE)
                other_screen("main screen?")

        for event in pygame.event.get():

            # print(f"got event: {event} ..")
            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.display.update()

if __name__=="__main__":
    main()
