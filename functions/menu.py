import sys
import pygame

# Definir colores
WHITE = (255, 255, 255)

# Inicializar PyGame
pygame.init()

# Configuración de la pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Fuente y tamaño del texto
font = pygame.font.Font(None, 36)


def draw_text(text, x, y):
    """
    Función para desplegar texto en la pantalla del juego
    """
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)


def main_menu():
    """
    Función para desplegar el menú principal
    """
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                #quit()
                sys.exit()

        screen.fill((0, 0, 0))  # Fondo negro
        draw_text("Menú Principal", WIDTH // 2, HEIGHT // 4)
        draw_text("Presiona ESPACIO para jugar", WIDTH // 2, HEIGHT // 2)
        draw_text("Presiona ESC para salir", WIDTH // 2, HEIGHT * 3 // 4)
        pygame.display.update()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            running = False

        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            #quit()
            sys.exit()


def game_over_menu():
    """
    Función para desplegar el menú de game over
    """
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                #quit()
                sys.exit()

        screen.fill((0, 0, 0))  # Fondo negro
        draw_text("Game Over", WIDTH // 2, HEIGHT // 4)
        draw_text("Presiona ESPACIO para jugar de nuevo", WIDTH // 2, HEIGHT // 2)
        draw_text("Presiona ESC para salir", WIDTH // 2, HEIGHT * 3 // 4)
        pygame.display.update()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            running = False

        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            # quit()
            sys.exit()
