import pygame # Import modułu

pygame.init() # Inicjalizacja modułu

# Utworzenie okna o określonych wymiarach
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Nadanie nazwy oknu
pygame.display.set_caption('Pierwsza Gra')

# Zmienna określająca, czy należy zamknąć okno
game_status = True
# Kod wykonywany póki aplikacja jest uruchomiona
while game_status:
    pygame.event.get()

pygame.quit() # Zamknięcie aplikacji
quit() # Zamknięcie skryptu