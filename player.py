import pygame
from pygame import Vector2

class Player:
    def __init__(self, x, y, speed = 2):
        self.origin = pygame.image.load("grafiki/player.png")
        self.origin.set_colorkey((0,0,0))
        self.img = self.origin.copy()
        self.rect = self.img.get_rect(center=(x, y))
        self.speed = speed
        self.angle = 0

    def update(self, keys):
        move = Vector2(0, 0)
        forward = Vector2(0, -1)
        Vector2.rotate_ip(forward, -self.angle)
        # if keys[pygame.K_w]:
        #     #move.y = -1

        # if keys[pygame.K_s]:
        #     #move.y = 1       
        if keys[pygame.K_d]:
            #move.x = 1 
            self.angle -= 2
        if keys[pygame.K_a]:
            #move.x = -1 
            self.angle += 2

        if move.length_squared() > 0:
            Vector2.normalize_ip(move)
        self.rect.center += forward * self.speed

        #self.angle += 2
        center = self.rect.center
        self.img = pygame.transform.rotate(self.origin, self.angle)
        self.rect = self.img.get_rect(center = center)
        #self.rect.center = center
        