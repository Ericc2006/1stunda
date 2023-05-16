import pygame
import sys
import random

# Iestatījumi
screen_width = 640
screen_height = 480
field_width = 640
field_height = 480
ball_size = 25
paddle_width = 15
paddle_height = 80
paddle_speed = 0.5
ball_speed_x = 0.2
ball_speed_y = 0.2


# Krāsas definīcijas
DARKBLUE = (31, 97, 141)
WHITE = (251, 252, 252)

# Spēlētāju sākuma pozīcijas
player1_x = 0
player1_y = field_height / 2 - paddle_height / 2
player2_x = field_width - paddle_width
player2_y = field_height / 2 - paddle_height / 2

# Bumbiņas sākuma pozīcijas
ball_x = screen_width / 2 - ball_size / 2
ball_y = screen_height / 2 - ball_size / 2

# Spēlētāju rezultāti
player1_score = 0
player2_score = 0

# Inicializējam pygame
pygame.init()

# Izveidojam ekrānu
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Galda teniss')

player2_y = field_height / 2 - paddle_height / 2



def ai_move():
    global player2_y
    error = random.choice([-1, 0, 0, 0, 1, 1, 2, 3, 4])  # Pievienojiet šo rindiņu, lai ģenerētu gadījuma skaitli
    paddle_speed = 0.1
    if player2_y + paddle_height / 2 + error > ball_y + ball_size:
        player2_y -= paddle_speed
    if player2_y + paddle_height / 2 + error < ball_y:
        player2_y += paddle_speed



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        # Spēlētājs 1 pārvietojas uz augšu
        player1_y -= paddle_speed
    if keys[pygame.K_DOWN]:
        # Spēlētājs 1 pārvietojas uz leju
        player1_y += paddle_speed

    ai_move()  # Izsaukums AI spēlētāja pārvietošanai

    # Bumbiņas kustība
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Detektē sadursmes ar laukuma malām
    if ball_x < 0:
        # Bumbiņa sasniedzis kreiso laukuma malu - player2 (labais spēlētājs) iegūst punktu
        player2_score += 1
        ball_x = screen_width / 2 - ball_size / 2
        ball_y = screen_height / 2 - ball_size / 2
        ball_speed_x = -ball_speed_x

    if ball_x + ball_size > field_width:
        # Bumbiņa sasniedzis labo laukuma malu - player1 (kreisais spēlētājs) iegūst punktu
        player1_score += 1
        ball_x = screen_width / 2 - ball_size / 2
        ball_y = screen_height / 2 - ball_size / 2
        ball_speed_x = -ball_speed_x

    if ball_y < 0 or ball_y + ball_size > field_height:
        # Bumbiņa sasniedzis augšējo vai apakšējo laukuma malu - mainām bumbiņas vertikālo kustības virzienu
        ball_speed_y = -ball_speed_y

    # Detektē sadursmi ar spēlētāju 1 (kreiso spēlētāju)
    if ball_x < player1_x + paddle_width and \
       player1_y < ball_y + ball_size and \
       ball_y < player1_y + paddle_height:
        # Sadursme ar spēlētāju 1 - mainām bumbiņas horizontālo kustības virzienu
        ball_speed_x = abs(ball_speed_x)

    # Detektē sadursmi ar spēlētāju 2 (labo spēlētāju)
    if ball_x + ball_size > player2_x and \
       player2_y < ball_y + ball_size and \
       ball_y < player2_y + paddle_height:
        # Sadursme ar spēlētāju 2 - mainām bumbiņas horizontālo kustības virzienu
        ball_speed_x = -abs(ball_speed_x)

    # Zīmējam visus objektus uz ekrāna
    screen.fill(DARKBLUE)
    pygame.draw.rect(screen, WHITE, pygame.Rect(player1_x, player1_y, paddle_width, paddle_height))
    pygame.draw.rect(screen, WHITE, pygame.Rect(player2_x, player2_y, paddle_width, paddle_height))
    pygame.draw.ellipse(screen, WHITE, pygame.Rect(ball_x, ball_y, ball_size, ball_size))
    pygame.draw.aaline(screen, WHITE, (field_width / 2, 0), (field_width / 2, field_height))
    pygame.draw.rect(screen, WHITE, pygame.Rect(0, 0, field_width, field_height), 2)
    pygame.display.flip()

    # Pārbaudām uzvarētāju
    if player1_score >= 10 or player2_score >= 10:
        pygame.quit()
        sys.exit()
