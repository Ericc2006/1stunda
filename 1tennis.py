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
ball_speed_x = 0.4
ball_speed_y = 0.4


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

player1_name = input("Ievadiet 1. spēlētāja vārdu: ")
player2_name = "AI"

# Inicializējam pygame
pygame.init()

# Izveidojam ekrānu
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Galda teniss')

player2_y = field_height / 2 - paddle_height / 2


paddle_speed = 0.5

def ai_move():
    global player2_y
    error = random.choice([-1, 0, 0, 0, 1, 1, 2, 3, 4]) 
    paddle_speed = 0.3
    if player2_y + paddle_height / 2 + error > ball_y + ball_size:
        player2_y -= paddle_speed
    if player2_y + paddle_height / 2 + error < ball_y:
        player2_y += paddle_speed

def display_last_results():
    filename = "rezultati.txt"
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            last_results = lines[-5:]  
            print("Pēdējie rezultāti:")
            for result in last_results:
                print(result.strip())
    except FileNotFoundError:
        print("Nav iepriekšējo rezultātu.")





while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            filename = "rezultati.txt"
            with open(filename, "a") as file:
                file.write(f"{player1_name} {player1_score} - {player2_score} {player2_name}\n")
            pygame.quit()
            display_last_results()
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

    # Attēlo rezultātus uz ekrāna
    font = pygame.font.Font(None, 36)
    player1_score_text = font.render(player1_name + " " + str(player1_score), True, WHITE)
    player2_score_text = font.render(player2_name + " " + str(player2_score), True, WHITE)
    screen.blit(player1_score_text, (20, 20))
    screen.blit(player2_score_text, (screen_width - player2_score_text.get_width() - 20, 20))

    pygame.display.flip()
    # Pārbaudām uzvarētāju


# Pārbauda uzvarētāju
    if player1_score >= 10 or player2_score >= 10:
        filename = "rezultati.txt"
        with open(filename, "a") as file:
            file.write(f"{player1_name} {player1_score} - {player2_score} {player2_name}\n")
        winner_text = ""
        if player1_score > player2_score:
            winner_text = player1_name + " wins!"
        else:
            winner_text = player2_name + " wins!"

        font = pygame.font.Font(None, 48)
        winner_text_render = font.render(winner_text, True, WHITE)
        winner_text_pos = (screen_width // 2 - winner_text_render.get_width() // 2, screen_height - 100)
        screen.blit(winner_text_render, winner_text_pos)

        pygame.display.flip()

        pygame.time.wait(3000)
        display_last_results()

        pygame.quit()
        sys.exit()



