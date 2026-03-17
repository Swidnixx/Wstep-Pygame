import pygame

class TextDrawer:
    def __init__(self, screen,):
        self.screen = screen
        self.main_font = pygame.font.SysFont("Verdana", 28)

    def draw_text_main(self, text, position, color=(0,0,0)):
        text = self.main_font.render(text, True, color)
        self.screen.blit(text, position)
