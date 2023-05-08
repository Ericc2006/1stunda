import pygame
import random

# Uzstādījumi
WIDTH = 800
HEIGHT = 600
FPS = 60

# Krāsu definīcijas
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Inicializējiet Pygame moduli
pygame.init()

# Izveidojiet logu
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Galda teniss")

# Ielādējiet skaņas efektus
hit_sound = pygame.mixer.Sound("hit.wav")
score_sound = pygame.mixer.Sound("score.mp3")

# Izveidojiet spēles objektus
ball = pygame.Rect(WIDTH/2 - 10, HEIGHT/2 - 10, 20, 20)
player1 = pygame.Rect(50, HEIGHT/2 - 50, 10, 100)
player2 = pygame.Rect(WIDTH - 60, HEIGHT/2 - 50, 10, 100)

# Definējiet spēlētāju punktu skaitītājus
player1_score = 0
player2_score = 0

# Izveidojiet fontu punktu skaitītājiem
font = pygame.font.SysFont("Arial", 50)

# Definējiet spēles līmeņus un sarežģītību
level = 1
speed = 5
time_limit = 60

# Definējiet spēles stāvokli
game_over = False

# Definējiet funkciju bumbas trajektorijas maiņai, ja tā saskaras ar spēlētāja malu
def change_ball_direction():
    global speed, hit_sound

    # Pievienojiet nejaušu leņķi bumbas trajektorijai
    angle = random.randint(-60, 60)
    speed = -speed
    speed_y = speed * math.sin(math.radians(angle))
    speed_x = speed * math.cos(math.radians(angle))
    ball_direction = [speed_x, speed_y]
    hit_sound.play()

    # Ja bumba saskaras ar kreiso spēlētāja malu, mainiet bumbas trajektoriju un atjaunojiet punktu skaitītāju
    if ball.left < 0:
        player2_score += 1
        score_sound.play()
        ball.center = (WIDTH/2, HEIGHT/2)
        speed = -speed

        # Pievienojiet nejaušu leņķi bumbas trajektorijai
        angle = random.randint(-60, 60)
        speed = -speed
        speed_y = speed * math.sin(math.radians(angle))
        speed_x = speed * math.cos(math.radians(angle))
        ball_direction = [speed_x, speed_y]

    # Ja bumba saskaras ar labo spēlētāja malu, mainiet bumbas trajektoriju un atjaunojiet punktu skaitītāju
    if ball.right > WIDTH:
        player1_score += 1
        score_sound.play()
        ball.center = (WIDTH/2, HEIGHT/2)
        speed = -speed

        # Pievienojiet nejaušu leņķi bumbas trajektorijai
        angle = random.randint(-60, 60)
        speed = -speed
        speed_y = speed * math.sin(math.radians(angle))
        speed_x = speed * math.cos(math.radians(angle))
        ball_direction = [speed_x, speed_y]

    # Ja bumba saskaras ar augšējo vai apakšējo spēlētāja malu, mainiet bumbas trajektoriju un atskaņojiet skaņas efektu
    if ball.top < 0 or ball.bottom > HEIGHT:
        ball_direction[1] = -ball_direction[1]
        hit_sound.play()

    # Pārbaudiet, vai bumba saskaras ar spēlētāju
    if ball.colliderect(player1) or ball.colliderect(player2):
        change_ball_direction()

    # Atjaunojiet punktu skaitītājus un spēles laiku
    player1_text = font.render(str(player1_score), True, WHITE)
    player2_text = font.render(str(player2_score), True, WHITE)
    screen.blit(player1_text, (WIDTH/4, 10))
    screen.blit(player2_text, (3*WIDTH/4, 10))
    time_limit -= 1/FPS

    # Pārbaudiet, vai laiks ir beidzies un noteikti uzvarētāju
    if time_limit <= 0:
        if player1_score > player2_score:
            winner_text = font.render("Player 1 Wins!", True, WHITE)
        elif player2_score > player1_score:
            winner_text = font.render("Player 2 Wins!", True, WHITE)
        else:
            winner_text = font.render("Tie Game!", True, WHITE)
        screen.blit(winner_text, (WIDTH/2 - 150, HEIGHT/2))
        pygame.display.update()
        pygame.time.delay(3000)
        ball.center = (WIDTH/2, HEIGHT/2)
        player1.center = (50, HEIGHT/2 - 50)
        player2.center = (WIDTH - 60, HEIGHT/2 - 50)
        player1_score = 0
        player2_score = 0
        speed = 5
        time_limit = 60
        level += 1

    # Izvēlieties līmeni un pielāgojiet spēles sarežģītību
    if level == 2:
        speed = 7
        time_limit = 45
    elif level == 3:
        speed = 10
        time_limit = 30
    elif level == 4:
        speed = 15
        time_limit = 20

    # Izvēlieties līmeni un pielāgojiet spēles sarežģītību
    if level == 2:
        speed = 7
        time_limit = 45
    elif level == 3:
        speed = 10
        time_limit = 30
    elif level == 4:
        speed = 15
        time_limit = 20

    # Zīmējiet spēles objektus uz ekrāna
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, player1)
    pygame.draw.rect(screen, WHITE, player2)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH/2, 0), (WIDTH/2, HEIGHT))
    pygame.display.update()

    # Ierobežo FPS uz dotajiem uzstādījumiem
    pygame.display.update()
    clock.tick(FPS)

# Iziet no Pygame moduļa
pygame.quit()

