import pygame
import math

#temporary solution for scaling window
scalar = 32
    
# Window managment:
pygame.init()
screen_width = 800*scalar/32
screen_height = 600*scalar/32
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('ufo.png') 
pygame.display.set_icon(icon)

#Player
player_img_og = pygame.image.load('player.png')
player_img_scaled = pygame.transform.scale(player_img_og,(scalar,scalar/2)) 
player_img = player_img_scaled
player_x = 370
player_y = 480
player_x_change = 0

#Enemy_FrontRow
enemy_img = []
enemy_x = []
enemy_y = []
num_of_enemies = 6
enemy_speed = 2
enemy_direction = 1

for i in range(num_of_enemies):
    enemy_img_original = pygame.image.load('enemy.png')
    enemy_img_scaled = pygame.transform.scale(enemy_img_original, (scalar, scalar))
    enemy_img.append(enemy_img_scaled)
    enemy_x.append(2*scalar + i * scalar*5/3)
    enemy_y.append(50)

#Bullet
bullet_img_og = pygame.image.load('bullet.png')
bullet_img_scaled = pygame.transform.scale(bullet_img_og, (scalar/4,scalar/2))
bullet_img = bullet_img_scaled
bullet_x = 0
bullet_y = 480
bullet_y_change = 2
bullet_state = "ready" 

#Score_Counter
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
text_x = 10
text_y = 10

#Functions:

#Render:
def player(x, y):
    screen.blit(player_img, (x, y))

def enemy(x, y, i):
    screen.blit(enemy_img[i], (x, y))

#Shoting
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (x+12, y + 12))

#Collision
def is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = math.sqrt(math.pow(enemy_x - bullet_x, 2) + math.pow(enemy_y - bullet_y, 2))
    return distance < 27

#ShowScore
def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

#END_MESSAGE
def show_message(message):
    message_font = pygame.font.Font('freesansbold.ttf', 64)
    message_text = message_font.render(message, True, (255, 255, 255))
    screen.blit(message_text, (screen_width / 2 - message_text.get_width() / 2, screen_height / 2 - message_text.get_height() / 2))
    pygame.display.update()
    pygame.time.delay(3000)

# Główna pętla gry
running = True
while running:
    # Kolor tła
    screen.fill((0, 0, 0))
    
    # Sprawdzenie zdarzeń
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -5
            if event.key == pygame.K_RIGHT:
                player_x_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_x = player_x
                    fire_bullet(bullet_x, bullet_y)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0

    # Ruch gracza
    player_x += player_x_change
    if player_x <= 0:
        player_x = 0
    elif player_x >= screen_width - 64:
        player_x = screen_width - 64

    # Ruch wroga
    change_direction = False
    for i in range(len(enemy_x)):
        enemy_x[i] += enemy_speed * enemy_direction
        if enemy_x[i] <= 0 or enemy_x[i] >= screen_width - 64:
            change_direction = True
    
    if change_direction:
        enemy_direction *= -1
        for i in range(len(enemy_x)):
            enemy_y[i] += 40

    # Sprawdzenie kolizji i usuwanie trafionych kosmitów
    for i in range(len(enemy_x) - 1, -1, -1):
        if is_collision(enemy_x[i], enemy_y[i], bullet_x, bullet_y):
            bullet_y = 480
            bullet_state = "ready"
            score_value += 1
            enemy_x.pop(i)
            enemy_y.pop(i)
            enemy_img.pop(i)

    # Sprawdzenie, czy któryś kosmita dotknął gracza
    for i in range(len(enemy_x)):
        if enemy_y[i] >= player_y - 64:
            show_message("Przegrana :(")
            running = False

    # Sprawdzenie, czy wszyscy kosmici zostali pokonani
    if len(enemy_x) == 0:
        show_message("Gratulacje!!!")
        running = False

    # Ruch pocisku
    if bullet_state == "fire":
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change
    if bullet_y <= 0:
        bullet_y = 480
        bullet_state = "ready"

    player(player_x, player_y)

    for i in range(len(enemy_x)):
        enemy(enemy_x[i], enemy_y[i], i)

    show_score(text_x, text_y)
    
    pygame.display.update()
    
pygame.quit()
