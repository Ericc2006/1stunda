def game():
    # ... iepriekšējās kodu daļas ...

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

        # Pārbaudām spēlētāju raktu kustību
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player1_y -= paddle_speed
        if keys[pygame.K_s]:
            player1_y += paddle_speed
        if keys[pygame.K_UP]:
            player2_y -= paddle_speed
        if keys[pygame.K_DOWN]:
            player2_y += paddle_speed

        # Pārbaudām spēlētāju raktu atrašanās vietu
        if player1_y < 0:
            player1_y = 0
        if player1_y > screen_height - paddle_height:
            player1_y = screen_height - paddle_height
        if player2_y < 0:
            player2_y = 0
        if player2_y > screen_height - paddle_height:
            player2_y = screen_height - paddle_height

        # Atjaunojam bumbiņas pozīciju
        ball_x += ball_speed_x
        ball_y += ball_speed_y

        # Pārbaudām sadursmi ar sienām
        if ball_x <= 0 or ball_x >= screen_width:
            ball_speed_x *= -1

        # Pārbaudām sadursmi ar raketēm
        if check_collision(ball_x, ball_y, player1_x, player1_y) or check_collision(ball_x, ball_y, player2_x, player2_y):
            ball_speed_x *= -1

        # Pārbaudām, vai bumba ir izgājusi ārpus spēles laukuma
        if ball_x < 0:
            print("Spēlētājs 2 uzvar!")
            pygame.quit()
            sys.exit()
        elif ball_x > screen_width:
            print("Spēlētājs 1 uzvar!")
            pygame.quit()
            sys.exit()

        # Atjaunojam ekrānu
        draw_table()
        draw_ball(ball_x, ball_y)
        draw_paddle(player1_x, player1_y)
        draw_paddle(player2_x, player2_y)
        pygame.display.flip()

        # Kontrolējam spēles ātrumu
        pygame.time.Clock().tick(60)

# Palaižam spēli
if __name__ == '__main__':
    game()
