import sys
import pygame
import random
from Class import Crosshair, Target

WHITE = (255, 255, 255)

# General Setup

pygame.init()
clock = pygame.time.Clock()
font = pygame.font.Font("freesansbold.ttf", 32)

# GAME SCREEN

screen_width = 1920
screen_height = 1080

screen = pygame.display.set_mode((screen_width, screen_height))
# background img
background = pygame.image.load("PNG/Stall/bg_blue.png")
# scale the img to fit the whole screen
background = pygame.transform.scale(background, (1920, 1080))

# hide the mouse hover
pygame.mouse.set_visible(False)

# crosshair Group
crosshair = Crosshair("PNG/HUD/crosshair_white_large.png")
# creating the group for the Sprites
crosshair_group = pygame.sprite.Group()
# adding the class to the group
crosshair_group.add(crosshair)



score = 0
start_time = None
# ------------ Target group___________________
target_group = pygame.sprite.Group()

for target in range(2):
    pos_x = random.randint(1, screen_width)
    pos_y = random.randint(1, screen_height)
    target_ = Target("PNG/Objects/target_red2.png", pos_x, pos_y)
    target_group.add(target_)

Game = True


while Game:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # fire
        if event.type == pygame.MOUSEBUTTONDOWN:

            if pygame.sprite.spritecollide(crosshair, target_group, True):
                score += 1
                crosshair.shoot_sound()
                start_time = pygame.time.get_ticks()



        # if not target_group:
        #     print("yes")
        #     font = pygame.font.Font(None, 74)
        #     text = font.render("Score: " + str(score), True, WHITE)
        #     screen.blit(text, (250, 300))

    # blit the background
    screen.blit(background, (0, 0))

    # draw the Sprite group
    target_group.draw(screen)
    crosshair_group.draw(screen)

    crosshair_group.update()

    if not target_group:

        font = pygame.font.Font(None, 74)
        text = font.render("Score: " + str(score), True, WHITE)
        screen.blit(text, (250, 300))
        time_since_enter = pygame.time.get_ticks() - start_time
        message = 'Milliseconds since enter: ' + str(time_since_enter)
        screen.blit(font.render(message, True, WHITE), (500, 500))
        Game = False






    # update the screen
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
