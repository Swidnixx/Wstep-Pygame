import pygame
from pygame import Vector2

class Player:
    def __init__(self, x, y, speed = 2):
        self.origin = pygame.image.load("grafiki/player.png")
        self.origin.set_colorkey((0,0,0))
        self.img = self.origin.copy()
        self.position = (x, y)
        self.rect = self.img.get_rect(center=self.position)
        self.speed = speed
        self.rotation = 0
        self.rotation_speed = 4

    def update(self, keys):
        self.keys = keys
        self.current_speed = self.speed
        self.steer()
        self.move()

    def steer(self):
        if self.keys[pygame.K_d]: 
            self.rotation -= self.rotation_speed
        if self.keys[pygame.K_a]:
            self.rotation += self.rotation_speed

        if self.keys[pygame.K_w]:
            self.current_speed *= 2
        if self.keys[pygame.K_s]:
            self.current_speed = 0   

    def move(self):
        forward = Vector2(0, -1)
        Vector2.rotate_ip(forward, -self.rotation)
        self.position += forward * self.current_speed

        self.img = pygame.transform.rotate(self.origin, self.rotation)
        self.rect = self.img.get_rect(center=self.position)



    
        