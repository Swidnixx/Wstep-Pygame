import pygame
from pygame import Vector2

class Player:
    def __init__(self, x, y, speed = 5):
        self.img = pygame.image.load("grafiki/player.png")
        self.img.set_colorkey((0,0,0))
        self.rect = self.img.get_rect(center=(x, y))
        self.speed = speed

    def update(self, keys):
        move = Vector2(0, 0)
        if keys[pygame.K_w]:
            move.y = -1
        if keys[pygame.K_s]:
            move.y = 1       
        if keys[pygame.K_d]:
            move.x = 1 
        if keys[pygame.K_a]:
            move.x = -1 

        if move.length_squared() > 0:
            Vector2.normalize_ip(move)
        self.rect.center += move * self.speed