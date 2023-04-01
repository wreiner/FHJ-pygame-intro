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
