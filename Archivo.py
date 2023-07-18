import pygame
import sys
from Button import Button
import random
import math


pygame.init()

SCREEN = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("Alien_01.png")
pygame.display.set_icon(icon)
BG = pygame.image.load("Nebula_2.png")
BG_menu = pygame.image.load("Nebula_Pimk.png")


def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)


def add_new_user():
    new_username = ""

    while True:
        SCREEN.blit(BG, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    new_username2 = new_username.lower()
                    new_username3 = new_username2.capitalize()
                    # Guardar el nombre de usuario en un archivo de texto
                    with open("username", "a") as file:
                        file.write(f'{new_username3} \n')
                    print("New Username:", new_username)
                    return
                elif event.key == pygame.K_BACKSPACE:
                    new_username = new_username[:-1]
                else:
                    new_username += event.unicode

        text_surface = get_font(20).render("Enter username: ", True, "#d7fcd4")
        SCREEN.blit(text_surface, (260, 250))
        # Obtén las dimensiones del texto renderizado
        text_width, text_height = text_surface.get_size()
        # Calcula la nueva coordenada y para que aparezca abajo del texto
        new_y = 250 + text_height + 10  # Agrega un espacio de 10 píxeles
        # Renderiza el new_username debajo del texto original
        username_surface = get_font(20).render(new_username, True, "#d7fcd4")
        SCREEN.blit(username_surface, (260, new_y))
        text_cuadrado = pygame.image.load("assets/Play Rect.png")
        SCREEN.blit(text_cuadrado, (215, 230))
        pygame.display.update()


def game():
    end_font = pygame.font.Font("assets/font.ttf", 64)
    end_font = pygame.font.Font("assets/font.ttf", 64)

    def final_message():
        final_text = end_font.render(f"GAME OVER", True, "#cb3234")
        SCREEN.blit(final_text, (120, 200))

    def final_message_win():
        victory_text = end_font.render("YOU WIN!", True, "#10771A")
        SCREEN.blit(victory_text, (120, 200))

    # Player variables
    img_player = pygame.image.load("Spaceship_03.png")
    player_x = 360  # 400 - 32 para que quede centrado
    player_y = 525  # 600- 64 para que quede centrado
    player_x_change = 0

    # Enemy variables
    img_enemy = []
    enemy_x = []
    enemy_y = []
    enemy_x_change = []
    enemy_y_change = []
    number_of_enemies = 10
    enemy_speed = 1.8  # Velocidad inicial de los enemigos
    global_enemy_speed = enemy_speed  # Velocidad global de los enemigos
    speed_increase_factor = 1.5  # Factor de aumento de velocidad

    for i in range(number_of_enemies):
        img_enemy.append(pygame.image.load("Alien_01.png"))
        enemy_x.append(random.randint(0, 736))
        enemy_y.append(random.randint(30, 200))
        enemy_x_change.append(enemy_speed)
        enemy_y_change.append(1.8)

    # Bullet variables
    img_bullet = pygame.image.load("Laser_Blue.png")
    bullet_x = 0
    bullet_y = 0
    bullet_x_change = 0
    bullet_y_change = 15
    bullet_visible = False

    # Score Variables
    score = 0
    score_font = pygame.font.Font("freesansbold.ttf", 32)
    score_text_x = 10
    score_text_y = 10

    # Level Variable
    level = 1

    # Meteor variables
    img_asteroid = pygame.image.load("Asteroid_Fire_Blue_64.png")
    asteroid_x = []
    asteroid_y = []
    visible_asteroid = False

    # Show score
    def show_score(x, y):
        text = score_font.render(f"Score: {score}", True, "#d7fcd4")
        SCREEN.blit(text, (x, y))

    # Show level
    def show_level(x, y):
        level_text = score_font.render(f"Level: {level}", True, "#d7fcd4")
        SCREEN.blit(level_text, (x, y + 50))

    # Show meteoritos
    def show_asteroid():
        if visible_asteroid:
            for i in range(len(asteroid_x)):
                asteroid_y[i] += 5  # Ajusta la velocidad de caída de los meteoritos
                SCREEN.blit(img_asteroid, (asteroid_x[i], asteroid_y[i]))
                if asteroid_y[i] > 600:
                    # Eliminar el meteorito si sale de la pantalla
                    asteroid_x.pop(i)
                    asteroid_y.pop(i)
                    break

            # Crear nuevos meteoritos
            if len(asteroid_x) < 10:  # Número máximo de meteoritos en pantalla
                asteroid_x.append(random.randint(50, 750))
                asteroid_y.append(random.randint(-200, -50))

    # Show player in screen
    def player(x, y):
        SCREEN.blit(img_player, (x, y))

    # Show enemy
    def enemy(x, y, enemy_index):
        SCREEN.blit(img_enemy[enemy_index], (x, y))

    # Shoot Bullet
    def shoot_bullet(x, y):
        nonlocal bullet_visible
        bullet_visible = True
        SCREEN.blit(img_bullet, (x + 23, y + 10))

    # Detect collision
    def detect_collision(x_1, y_1, x_2, y_2):
        x_sub = x_2 - x_1
        y_sub = y_2 - y_1
        distance = math.sqrt(math.pow(x_sub, 2) + math.pow(y_sub, 2))
        if distance < 27:
            return True
    # Game loop
    is_running = True
    while is_running:
        SCREEN.blit(BG, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player_x_change -= 7.0
                if event.key == pygame.K_RIGHT:
                    player_x_change += 7.0
                if event.key == pygame.K_SPACE:
                    if not bullet_visible:
                        bullet_x = player_x
                    shoot_bullet(bullet_x, bullet_y)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                    player_x_change = 0

        # Update player location
        player_x += player_x_change

        # Keep player inside the screen
        if player_x <= 0:
            player_x = 0
        elif player_x >= 736:
            player_x = 736

        for i in range(number_of_enemies):
            # Update enemy location
            enemy_x[i] += global_enemy_speed * enemy_x_change[i]

            # Keep enemies inside the screen
            if enemy_x[i] <= 0:
                enemy_x_change[i] += 0.3
                enemy_y[i] += enemy_y_change[i]
            elif enemy_x[i] >= 736:
                enemy_x_change[i] -= 0.3
                enemy_y[i] += enemy_y_change[i]

            # Detect collision
            collision = detect_collision(enemy_x[i], enemy_y[i], bullet_x, bullet_y)
            if collision:
                enemy_x[i] = random.randint(0, 736)
                enemy_y[i] = random.randint(30, 200)
                bullet_visible = False
                score += 1
                bullet_y = 500

                if score % 10 == 0:
                    level += 1
                    global_enemy_speed *= speed_increase_factor  # Aumentar la velocidad global de los enemigos

            if score == 30 and not visible_asteroid:
                visible_asteroid = True
                # Crear 10 meteoritos y asignar sus coordenadas iniciales
                for j in range(10):
                    asteroid_x.append(random.randint(50, 750))
                    asteroid_y.append(random.randint(-200, -50))
            if score == 50:
                final_message_win()
                visible_asteroid = False
                break

            for j in range(len(asteroid_x)):
                collision2 = detect_collision(asteroid_x[j], asteroid_y[j], bullet_x, bullet_y)
                if collision2:
                    asteroid_x[j] = random.randint(50, 750)
                    asteroid_y[j] = random.randint(-200, 50)
                    bullet_visible = False
                    score += 1
                    bullet_y = 500

            if enemy_y[i] > 450:  # cuando rebase este punto pierdes
                for j in range(number_of_enemies):
                    enemy_y[j] = 1000  # que vaya hasta abajo de la pantalla como si desapareciera
                visible_asteroid = False
                final_message()
                break
            for h in range(len(asteroid_x)):
                collision_with_meteorite = detect_collision(asteroid_x[i], asteroid_y[i], player_x, player_y)
                if collision_with_meteorite:
                    enemy_y[h] = 1000
                    player_y = 1000
                    visible_asteroid = False
                    final_message()
                    break

            # Show enemy
            enemy(enemy_x[i], enemy_y[i], i)

