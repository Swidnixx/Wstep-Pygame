import pygame

class TextDrawer:
    def __init__(self):
        self.main_font = pygame.font.SysFont("Verdana", 28)

    def draw_text_main(self, screen, text, position, color=(0,0,0)):
        text = self.main_font.render(text, True, color)
        screen.blit(text, position)
