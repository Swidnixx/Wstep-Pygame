import pygame # Import modułu
from player import Player
from pickups import PickupFactory

pygame.init() # Inicjalizacja modułu

# Utworzenie okna o określonych wymiarach
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#Timer
clock = pygame.time.Clock()

# Nadanie nazwy oknu
pygame.display.set_caption('Pierwsza Gra')

#obiekty gry
player = Player(SCREEN_WIDTH//2, SCREEN_HEIGHT//2)
pickup_factory = PickupFactory(SCREEN_WIDTH, SCREEN_HEIGHT)

spawn_event = pygame.USEREVENT
pygame.time.set_timer(spawn_event, 3000)

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

    #rysowanie
    screen.fill([23, 54, 200])
    screen.blit(player.img, player.rect)
    for p in pickup_factory.pickups:
        screen.blit(p.img, p.rect)
    pygame.display.update() # Odświeżenie wyświetlanego okna
    clock.tick(60)


pygame.quit() # Zamknięcie aplikacji
quit() # Zamknięcie skryptu