import pygame
import random

# Konstantes
WIDTH = 800
HEIGHT = 400
BALL_RADIUS = 20
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 60
PADDLE_SPEED = 5
FPS = 60

# Krāsas
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Inicializējiet Pygame moduli
pygame.init()


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Galda teniss")
clock = pygame.time.Clock()

# Sākuma pozīcijas
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
paddle1_y = HEIGHT // 2 - PADDLE_HEIGHT // 2
paddle2_y = HEIGHT // 2 - PADDLE_HEIGHT // 2
ball_dx = random.choice([-1, 1])
ball_dy = random.choice([-1, 1])

# Spēles laika un uzvaras nosacījumi
game_time = 0
winning_score = 5
player1_score = 0
player2_score = 0

# Fonti
font_large = pygame.font.Font(None, 70)
font_small = pygame.font.Font(None, 36)

# Spēles galvenais cikls
running = True
while running:
    screen.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle1_y > 0:
        paddle1_y -= PADDLE_SPEED
    if keys[pygame.K_s] and paddle1_y < HEIGHT - PADDLE_HEIGHT:
        paddle1_y += PADDLE_SPEED
    if keys[pygame.K_UP] and paddle2_y > 0:
        paddle2_y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and paddle2_y < HEIGHT - PADDLE_HEIGHT:
        paddle2_y += PADDLE_SPEED
    
    ball_x += ball_dx
    ball_y += ball_dy
    
    # Bumbas atstarpe no malām
    if ball_y < BALL_RADIUS or ball_y > HEIGHT - BALL_RADIUS:
        ball_dy *= -1
    
    # Bumbas sadursme ar pārlikšanās vienu reizi
    if ball_x < PADDLE_WIDTH and paddle1_y < ball_y < paddle1_y + PADDLE_HEIGHT:
        ball_dx *= -1
    if ball_x > WIDTH - PADDLE_WIDTH - BALL_RADIUS and paddle2_y < ball_y < paddle2_y + PADDLE_HEIGHT:
        ball_dx *= -1
    
    # Pārbaudīt uzvaru
    if ball_x < 0:
        player2_score += 1
        if player2_score == winning_score:
            winner_text = font_large.render("Spēlētājs 2 uzvar!", True, WHITE)
            screen.blit(winner_text, (WIDTH // 2 - winner_text.get_width() // 2, HEIGHT // 2 - winner_text.get_height() // 2))
            running = False
       
