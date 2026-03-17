import pygame, random

class PickupFactory:
    def __init__(self, screen_w, screen_h):
        self.SCREEN_W = screen_w
        self.SCREEN_H = screen_h
        self.imgs = []
        for i in range(1,4):
            img = pygame.image.load(f'grafiki/bonus_{i}.png')
            self.imgs.append(img)
        
        self.pickups = []

    def spawn(self):
        img = random.choice(self.imgs)
        position = [random.randint(50, self.SCREEN_W-50),
                    random.randint(50, self.SCREEN_H-50)]
        self.pickups.append(Pickup(img, position))
    
class Pickup:
    def __init__(self, img, position):
        self.img = img.copy()
        self.rect = self.img.get_rect(center=position)