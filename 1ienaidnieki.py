import pygame
import random

# Inicializējam Pygame
pygame.init()

# Iestatām loga izmēru
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Iestatām spēles nosacījumus
PLAYER_SIZE = 50
PLAYER_SPEED = 5
PLAYER_COLOR = (255, 0, 0)

BONE_SIZE = 30
BONE_SPEED = 3
BONE_COLOR = (0, 0, 255)

# Izveidojam spēles objektus
player = pygame.Rect((WINDOW_WIDTH - PLAYER_SIZE) // 2, (WINDOW_HEIGHT - PLAYER_SIZE) // 2, PLAYER_SIZE, PLAYER_SIZE)

bones = []
for i in range(10):
    bone_x = random.randint(0, WINDOW_WIDTH - BONE_SIZE)
    bone_y = random.randint(0, WINDOW_HEIGHT - BONE_SIZE)
    bone = pygame.Rect(bone_x, bone_y, BONE_SIZE, BONE_SIZE)
    bones.append(bone)

# Spēles galvenais cikls
running = True
while running:
    # Pārbaudam notikumus
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Atjaunojam spēles stāvokli
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= PLAYER_SPEED
    if keys[pygame.K_RIGHT]:
        player.x += PLAYER_SPEED
    if keys[pygame.K_UP]:
        player.y -= PLAYER_SPEED
    if keys[pygame.K_DOWN]:
        player.y += PLAYER_SPEED

    # Pārvietojam kaulus
    for bone in bones:
        if bone.x > player.x:
            bone.x -= BONE_SPEED
        else:
            bone.x += BONE_SPEED

        if bone.y > player.y:
            bone.y -= BONE_SPEED
        else:
            bone.y += BONE_SPEED

    # Pārbaudam sadursmes
    for bone in bones:
        if player.colliderect(bone):
            running = False

    # Attēlojam spēles objektus
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, PLAYER_COLOR, player)
    for bone in bones:
        pygame.draw.rect(screen, BONE_COLOR, bone)
    pygame.display.flip()

# Izvadam beigu ziņu
print("Spēle beigusies!")

# Iziet no Pygame
pygame.quit()
