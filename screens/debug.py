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