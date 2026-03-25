import pygame
from pygame import Vector2
from globals import clock
from sounds import shoot_sounds         
import random

class Player:
    def __init__(self, x, y, speed=2):
        self.original = pygame.image.load("grafiki/player.png").convert_alpha()
        self.image = self.original.copy()
        
        self.position = Vector2(x, y)
        self.rect = self.image.get_rect(center=self.position)
        
        self.speed = speed
        self.rotation = 0
        self.rotation_speed = 4
        
        self.bullets = []
        self.shoot_cooldown_ms = 320
        self.last_shot_time = -10000
        
        self.keys = pygame.key.get_pressed()

    def update(self, keys):
        self.keys = keys
        self.current_speed = self.speed
        self._handle_input()
        self._move()

        # если хочешь считать время здесь — оставь, но для кулдауна оно не используется

    def _handle_input(self):
        if self.keys[pygame.K_d]:
            self.rotation -= self.rotation_speed
        if self.keys[pygame.K_a]:
            self.rotation += self.rotation_speed
        
        if self.keys[pygame.K_w]:
            self.current_speed *= 2
        if self.keys[pygame.K_s]:
            self.current_speed = 0
        
        if self.keys[pygame.K_SPACE]:
            self._try_shoot()

    def _try_shoot(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shot_time >= self.shoot_cooldown_ms:
            direction = Vector2(0, -1).rotate(-self.rotation)
            spawn_pos = self.position + direction * 34
            
            self.bullets.append(Bullet(spawn_pos, self.rotation))
            self.last_shot_time = current_time
            
            # Выбираем случайный звук выстрела
            random.choice(shoot_sounds).play()

    def _move(self):
        direction = Vector2(0, -1).rotate(-self.rotation)
        self.position += direction * self.current_speed

        rotated = pygame.transform.rotate(self.original, self.rotation)
        self.image = rotated.convert_alpha()
        self.rect = self.image.get_rect(center=self.position)

        self.bullets = [
            b for b in self.bullets
            if 0 <= b.rect.centerx <= 800 and 0 <= b.rect.centery <= 600
        ]
        
        for bullet in self.bullets:
            bullet.update()

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        for bullet in self.bullets:
            screen.blit(bullet.image, bullet.rect)


class Bullet:
    def __init__(self, position: Vector2, angle: float):
        self.image = pygame.Surface((20, 20), pygame.SRCALPHA)
        pygame.draw.rect(self.image, (255, 70, 70), (7, 2, 6, 16))
        
        rotated = pygame.transform.rotate(self.image, angle)
        self.image = rotated.convert_alpha()
        self.rect = self.image.get_rect(center=position)
        
        self.direction = Vector2(0, -1).rotate(-angle)
        self.speed = 5.5

    def update(self):
        self.rect.center += self.direction * self.speed