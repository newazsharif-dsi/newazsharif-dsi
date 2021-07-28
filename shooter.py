import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
bg_color = [0, 0, 0]

gun1_image = pygame.image.load('asset/gun1.png')
gun1_image = pygame.transform.scale(gun1_image, (100, 50))

bullet_image = pygame.image.load('asset/bullet.png')
bullet_image = pygame.transform.scale(bullet_image, (25, 10))


# Gun initial position
current_gun_x = 100
current_gun_y = 10
gun1_dx = 0
gun1_dy = 0

current_bullet_x = 205
current_bullet_y = 55

# bullet
bullet_dx = 0
bullet_dy = 0
def display_gun1(x, y):
    screen.blit(gun1_image, (x, y))

def display_bullet(x, y):
    screen.blit(bullet_image, (x, y))


#Bullet
initail_bullet_position = 0

is_triggered = False

gun_shot_sound = pygame.mixer.Sound('asset/gunshot.wav')
pygame.mouse.set_visible(False)

game_loop = True
while game_loop:
    screen.fill(bg_color)
    mx,my = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                is_triggered = True
                gun_shot_sound.play()
                display_gun1(current_gun_x - 50, current_gun_y)
                pygame.display.update()
                pygame.time.wait(100)
                current_bullet_x = current_gun_x+102
                current_bullet_y = current_gun_y+4

        if event.type == pygame.KEYUP:
            gun1_dx = 0
            gun1_dy = 0


    current_gun_x = mx
    current_gun_y = my
    display_gun1(current_gun_x, current_gun_y)


    if is_triggered and current_bullet_x <= 750:
        current_bullet_x += 1
        current_bullet_y += 0
        display_bullet(current_bullet_x, current_bullet_y)
    elif current_bullet_x > 750:
        is_triggered = False


    pygame.display.update()