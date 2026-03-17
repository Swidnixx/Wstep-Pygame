import pygame # Import modułu
from player import Player
from pickups import PickupFactory
from ui import TextDrawer

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
text_drawer = TextDrawer()

spawn_event = pygame.USEREVENT
pygame.time.set_timer(spawn_event, 3000)

score = 0
time = 0

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
    screen.blit(player.img, player.rect)
    for p in pickup_factory.pickups:
        screen.blit(p.img, p.rect)

    text_drawer.draw_text_main(screen, f'Score: {score}', (5, SCREEN_HEIGHT - 70), (196, 254, 255))
    text_drawer.draw_text_main(screen, f'Time: {time//1000}', (5, SCREEN_HEIGHT - 40), (196, 254, 255))

    pygame.display.update() # Odświeżenie wyświetlanego okna
    clock.tick(60)
    time += clock.get_time()


pygame.quit() # Zamknięcie aplikacji
quit() # Zamknięcie skryptu