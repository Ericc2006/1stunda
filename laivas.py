import pygame
import random

# Set up pygame
pygame.init()

# Set up display
WIDTH = 800
HEIGHT = 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Boat Game")

# Set up colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Set up boat
boat_width = 64
boat_height = 64
boat_x = WIDTH // 2 - boat_width // 2
boat_y = HEIGHT - boat_height
boat_speed = 5

# Set up obstacle
obstacle_width = 64
obstacle_height = 64
obstacle_x = random.randint(0, WIDTH - obstacle_width)
obstacle_y = -obstacle_height
obstacle_speed = 3

# Set up score
score = 0
font = pygame.font.Font(None, 36)

# Main game loop
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and boat_x > 0:
        boat_x -= boat_speed
    if keys[pygame.K_RIGHT] and boat_x < WIDTH - boat_width:
        boat_x += boat_speed

    win.fill(WHITE)

    # Update obstacle
    obstacle_y += obstacle_speed
    if obstacle_y > HEIGHT:
        obstacle_x = random.randint(0, WIDTH - obstacle_width)
        obstacle_y = -obstacle_height
        score += 1

    pygame.draw.rect(win, BLUE, (obstacle_x, obstacle_y, obstacle_width, obstacle_height))

    # Update boat
    pygame.draw.rect(win, BLUE, (boat_x, boat_y, boat_width, boat_height))

    # Display score
    score_text = font.render("Score: " + str(score), True, BLUE)
    win.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
