import pygame
from pygame import Vector2
from globals import clock

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

        self.bullets = []
        self.shoot_cooldown = 150
        self.time_since_shot = 0

    def update(self, keys):
        self.keys = keys
        self.current_speed = self.speed
        self.steer()
        self.move()

        self.time_since_shot += clock.get_time()

    def steer(self):
        if self.keys[pygame.K_d]: 
            self.rotation -= self.rotation_speed
        if self.keys[pygame.K_a]:
            self.rotation += self.rotation_speed

        if self.keys[pygame.K_w]:
            self.current_speed *= 2
        if self.keys[pygame.K_s]:
            self.current_speed = 0 

        if self.keys[pygame.K_SPACE]:
            self.shoot()  

    def move(self):
        forward = Vector2(0, -1)
        Vector2.rotate_ip(forward, -self.rotation)
        self.position += forward * self.current_speed

        self.img = pygame.transform.rotate(self.origin, self.rotation)
        self.rect = self.img.get_rect(center=self.position)

        for i in range(len(self.bullets)-1,-1,-1):
            b = self.bullets[i]
            b.update()
            in_screen = 0 < b.rect.centerx < 800 and 0 < b.rect.centery < 600
            if not in_screen:
                self.bullets.pop(i)

    def shoot(self):
        if self.time_since_shot > self.shoot_cooldown:
            self.bullets.append( Bullet(self.position, self.rotation) )
            self.time_since_shot = 0

    def draw(self, screen):
        screen.blit(self.img, self.rect)
        for b in self.bullets:
            screen.blit(b.img, b.rect)

class Bullet:
    def __init__(self, position, angle):
        self.img = pygame.Surface((20, 20))
        self.img.fill((0,0,0))
        strip = pygame.Surface((5,20))
        strip.fill((255,0,0))
        self.img.blit(strip, pygame.Rect(8,0,5,20))
        self.img.set_colorkey((0,0,0))
        self.img = pygame.transform.rotate(self.img, angle)
        self.rect = self.img.get_rect(center=position)
        self.direction = Vector2(0,-1).rotate(-angle)
        self.speed = 10

    def update(self):
        self.rect.center += self.direction * self.speed