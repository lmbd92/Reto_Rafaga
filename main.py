import pygame
from functions import game
from functions import menu

# Inicializar PyGame
pygame.init()

# Configuración de la pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Esquiva Obstáculos")

# Variables de estado del juego
in_game = False
game_over = False

while not game_over:
    if not in_game:
        menu.main_menu()
        in_game = True  # El juego comienza cuando el jugador presiona ESPACIO

    # Juego
    game.game_loop()

    # Cuando el juego termine
    menu.game_over_menu()
    in_game = False  # Reiniciar el juego

pygame.quit()
