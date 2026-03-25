import pygame
from player import Player
from pickups import PickupFactory
from ui import TextDrawer
from globals import *
from sounds import shoot_sounds 

pygame.init()
pygame.display.set_caption('Pierwsza Gra')

pygame.mixer.init()


pygame.mixer.music.load("sounds/background-music.mp3")
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)

pickup_sound = pygame.mixer.Sound("sounds/pickup.mp3")

clock = pygame.time.Clock()

spawn_event = pygame.USEREVENT
pygame.time.set_timer(spawn_event, 3000)

player = Player(SCREEN_WIDTH//2, SCREEN_HEIGHT//2)
pickup_factory = PickupFactory(SCREEN_WIDTH, SCREEN_HEIGHT)
text_drawer = TextDrawer(screen)

score = 0
time = 0

game_status = True

while game_status:
    events = pygame.event.get()
    for e in events:
        if e.type == pygame.QUIT:
            game_status = False
        if e.type == spawn_event:
            pickup_factory.spawn()
    
    keys = pygame.key.get_pressed()
    player.update(keys)

    collected = pickup_factory.check_collisions(player.rect)
    if collected > 0:
        score += collected
        pickup_sound.play()               # ← звук сбора

    screen.fill((0, 186, 214))
    player.draw(screen)
    for p in pickup_factory.pickups:
        screen.blit(p.img, p.rect)

    text_drawer.draw_text_main(f'Score: {score}', (5, SCREEN_HEIGHT - 70), (196, 254, 255))
    text_drawer.draw_text_main(f'Time: {time//1000}', (5, SCREEN_HEIGHT - 40), (196, 254, 255))
    text_drawer.draw_text_main(f'Bullets: {len(player.bullets)}', (5, 0), (196, 254, 255))

    pygame.display.update()
    clock.tick(60)
    # fps = clock.get_fps()
    # print(fps)

pygame.quit()