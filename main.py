import pygame # Import modułu

pygame.init() # Inicjalizacja modułu

# Utworzenie okna o określonych wymiarach
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#Timer
clock = pygame.time.Clock()

# Nadanie nazwy oknu
pygame.display.set_caption('Pierwsza Gra')

# Zmienna określająca, czy należy zamknąć okno
game_status = True
# Kod wykonywany póki aplikacja jest uruchomiona
while game_status:
# Odczytanie zdarzeń zarejestrowanych przez komputer
    events = pygame.event.get()
    for e in events:
        print(e)
        if e.type == pygame.QUIT:
            game_status = False
    
    screen.fill([23, 54, 200])
    pygame.display.update() # Odświeżenie wyświetlanego okna
    clock.tick(60)
    #clock.tick()
    print(clock.get_fps())

pygame.quit() # Zamknięcie aplikacji
quit() # Zamknięcie skryptu