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
player_img = pygame.transform.scale(pygame.image.load("assets/player.svg"), (50, 50))
obstacle_img = pygame.transform.scale(
    pygame.image.load("assets/obstacle.svg"), (30, 30)
)

# Variables del jugador
player_x = WIDTH // 2
player_y = HEIGHT - 50
player_speed = 5

# Variables de los obstáculos
obstacle_x = random.randint(0, WIDTH)
obstacle_y = 0
obstacle_speed = 3

# Variables para la puntuación
score = 0
font = pygame.font.Font(None, 36)


def draw_player():
    global player_x, player_y
    screen.blit(player_img, (player_x, player_y))


def draw_obstacle():
    global obstacle_x, obstacle_y
    screen.blit(obstacle_img, (obstacle_x, obstacle_y))


def display_score():
    score_text = font.render(f"Puntuación: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))


def game_over():
    global score, player_x, player_y, obstacle_x, obstacle_y
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        game_over_text = font.render("¡Game Over!", True, (255, 0, 0))
        replay_text = font.render("1. Jugar de nuevo", True, (0, 0, 0))
        exit_text = font.render("2. Salir", True, (0, 0, 0))

        screen.blit(game_over_text, (WIDTH // 2 - 100, HEIGHT // 2 - 100))
        screen.blit(replay_text, (WIDTH // 2 - 80, HEIGHT // 2 - 20))
        screen.blit(exit_text, (WIDTH // 2 - 40, HEIGHT // 2 + 20))

        pygame.display.update()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_1]:
            # Jugar de nuevo
            score = 0
            player_x = WIDTH // 2
            player_y = HEIGHT - 50
            obstacle_x = random.randint(0, WIDTH)
            obstacle_y = 0
            return

        if keys[pygame.K_2]:
            # Salir
            pygame.quit()
            quit()


def game_loop():
    global obstacle_y, obstacle_x, player_x, player_y, score
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
            score += 1

        if (
            player_x < obstacle_x < player_x + player_img.get_width()
            or player_x
            < obstacle_x + obstacle_img.get_width()
            < player_x + player_img.get_width()
        ) and obstacle_y + obstacle_img.get_height() > player_y:
            game_over()

        screen.fill(WHITE)
        draw_player()
        draw_obstacle()
        display_score()
        pygame.display.update()

    pygame.quit()
    quit()
