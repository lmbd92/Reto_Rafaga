import pygame
import random

# Definir las dimensiones de la ventana del juego
WIDTH, HEIGHT = 800, 600

# Colores
WHITE = (255, 255, 255)

# Inicializar PyGame
pygame.init()

# Configurar la pantalla
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Esquiva Obstáculos")

# Cargar las imágenes
player_img = pygame.image.load("assets/player.svg")
obstacle_img = pygame.image.load("assets/obstacle.svg")

# Variables del jugador
player_x = WIDTH // 2
player_y = HEIGHT - 50
player_speed = 5

# Variables de los obstáculos
obstacle_x = random.randint(0, WIDTH)
obstacle_y = 0
obstacle_speed = 3


def draw_player():
    screen.blit(player_img, (player_x, player_y))


def draw_obstacle():
    screen.blit(obstacle_img, (obstacle_x, obstacle_y))


def game_loop():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < WIDTH - player_img.get_width():
            player_x += player_speed

        obstacle_y += obstacle_speed
        if obstacle_y > HEIGHT:
            obstacle_x = random.randint(0, WIDTH)
            obstacle_y = 0

        screen.fill(WHITE)
        draw_player()
        draw_obstacle()
        pygame.display.update()

    pygame.quit()
    quit()
