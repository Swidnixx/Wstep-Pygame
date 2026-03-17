import pygame # Import modułu
from player import Player
from pickups import PickupFactory
from ui import TextDrawer
from globals import *

pygame.init() # Inicjalizacja modułu
pygame.display.set_caption('Pierwsza Gra')
spawn_event = pygame.USEREVENT
pygame.time.set_timer(spawn_event, 3000)

#obiekty gry
player = Player(SCREEN_WIDTH//2, SCREEN_HEIGHT//2)
pickup_factory = PickupFactory(SCREEN_WIDTH, SCREEN_HEIGHT)
text_drawer = TextDrawer(screen)

# Zmienna określająca, czy należy zamknąć okno
game_status = True
# Kod wykonywany póki aplikacja jest uruchomiona
while game_status:
    # Odczytanie zdarzeń zarejestrowanych przez komputer
    events = pygame.event.get()
    for e in events:
        if e.type == pygame.QUIT:
            game_status = False
        if e.type == spawn_event:
            pickup_factory.spawn()
    
    #logika
    keys = pygame.key.get_pressed()
    player.update(keys)

    collected = pickup_factory.check_collisions(player.rect)
    score += collected

    #rysowanie
    screen.fill((0, 186, 214))
    player.draw(screen)
    for p in pickup_factory.pickups:
        screen.blit(p.img, p.rect)

    #UI
    text_drawer.draw_text_main(f'Score: {score}', (5, SCREEN_HEIGHT - 70), (196, 254, 255))
    text_drawer.draw_text_main(f'Time: {time//1000}', (5, SCREEN_HEIGHT - 40), (196, 254, 255))
    text_drawer.draw_text_main(f'Bullets: {len(player.bullets)}', (5, 0), (196, 254, 255))

    pygame.display.update() # Odświeżenie wyświetlanego okna
    clock.tick(60)
    time += clock.get_time()


pygame.quit() # Zamknięcie aplikacji
quit() # Zamknięcie skryptu