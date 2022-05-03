import random

import pygame
from functions import Invader, Enemy, Bullet

pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("INVADERS")
clock = pygame.time.Clock()

run = True

BLACK = (0, 0, 0)

# This is a list of every sprite. All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()

# Sprite group

invader = Invader("files/player.png")
invader.rect.x = 400
invader.rect.y = 500

enemy_count = 5
all_sprites_list.add(invader)

enemy = Enemy("files/enemy.png", 20, 20)
enemy_group = pygame.sprite.Group()

for enemy in range(enemy_count):
    pos_x = random.randint(1, screen_width)
    # will increase this number so the enemy come down to the player in the Enemy class
    pos_y = 200
    one_enemy = Enemy("files/enemy.png", pos_x, pos_y)
    enemy_group.add(one_enemy)
# bullet
bullet_group = pygame.sprite.Group()

bullet = Bullet("files/bullet.png")
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        invader.move_right(7)
    if keys[pygame.K_RIGHT]:
        invader.move_right(-7)

    if keys[pygame.K_SPACE]:
        if bullet.bullet_state is "ready":
            bullet.rect.x = invader.rect.x + 15
            bullet.rect.y = invader.rect.y
            bullet_group.add(bullet)
            all_sprites_list.add(bullet)

    for buleet_ in bullet_group:
        enemy_hit = pygame.sprite.spritecollide(buleet_, enemy_group, True)


    # to change the bullet state to fire so we fire a bullet and update the y position
    if bullet.bullet_state is "fire":
        bullet_group.update()

    if not enemy_group:
        enemy_count += 2

    all_sprites_list.update()
    screen.fill(BLACK)
    enemy_group.update()
    enemy_group.draw(screen)
    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
