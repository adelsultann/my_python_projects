import pygame
import random
import math
from pygame import mixer

# initialize pygame

pygame.init()

# create the screen width and height
screen = pygame.display.set_mode((800, 600))

# Title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("Space-Invaders-Pygame-master/ufo.png")
pygame.display.set_icon(icon)

# background img 800,600
background = pygame.image.load("Space-Invaders-Pygame-master/background.png")

# Background Sound

mixer.music.load("Space-Invaders-Pygame-master/background.wav")
# -1 means work for infinity
#mixer.music.play(-1)

# Player
playerImg = pygame.image.load("Space-Invaders-Pygame-master/player.png")
# the position of the player
# we are going from 0 to 800 in the x axis 0 is left
playerX = 370
playerY = 500
PlayerX_change = 0

# enemy details
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load("Space-Invaders-Pygame-master/enemy.png"))
    # the position of the player
    # we are going from 0 to 800 in the x axis
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(1)
    enemyY_change.append(40)

# bullet details
bulletImg = pygame.image.load("Space-Invaders-Pygame-master/bullet.png")
bulletX = 0
# the bullet will be at the same position as the player
bulletY = 480
# the speed of the bullet
bulletY_change = 10
# ready you can't see the the bullet on the screen
# fire The bullet is currently moving
bullet_state = "ready"



# Score

score_value = 0
font = pygame.font.Font("freesansbold.ttf",32)
textX = 10
textY = 10

def sow_score(x,y):
    score = font.render("Score :" + str(score_value),True, (255,255,255))
    screen.blit(score, (x, y))


# game over
over_font = pygame.font.Font("freesansbold.ttf",64)


def game_over_text():
    game_over = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(game_over, (200,250))



def player(x, y):
    # blit is method to draw pic in the screen
    screen.blit(playerImg, (x, y))


def enemies(x, y, i):
    # blit is method to draw pic in the screen
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    # we increase the y so we make the bullet fire from the top not inside the ship
    screen.blit(bulletImg, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    # this is equation for the distance
    # https://www.mathplanet.com/education/algebra-2/conic-sections/distance-between-two-points-and-the-midpoint
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY, 2))
    # we come with 27 after trying and when we want to consider collision
    if distance < 27:
        return True
    else:
        return False




# loop to make the window keep running
running = True

while running:
    # change color of the window #RGB = red, green , blue from 0 to 255
    screen.fill((0, 0, 0))
    # background img
    screen.blit(background, (0, 0))
    # lopping through all the even in the pygame | pygame.even is method in pygame | every press in the keyboard is event
    for event in pygame.event.get():
        # if exit button is pressed
        if event.type == pygame.QUIT:
            running = False

        # if key is pressed check whether its right or left
        # KEYDOWN is pressed key | KEYUP is release
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                PlayerX_change -= 5
            if event.key == pygame.K_RIGHT:
                PlayerX_change += 5
                print("right press")
            if event.key == pygame.K_SPACE:
                # only if the state is ready you can fire bullet
                if bullet_state is "ready":
                    # add the sound of the fire
                    bullet_sound = mixer.Sound("Space-Invaders-Pygame-master/laser.wav")
                    bullet_sound.play()

                    # we saved the bulletX so we can control the
                    # the position of it
                    bulletX = playerX

                    fire_bullet(bulletX, bulletY)
        # KEYUP is release key
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                PlayerX_change = 0
                print("key has been released")

    # 5 = 5 + -0.1 -> 5 = 5 - 0.1
    # 5 = 5 + 0.1
    # move the player accordingly
    playerX += PlayerX_change
    # player set collision with the walls so it doesn't go out of bounds
    if playerX <= 0:
        playerX = 0
        # 736 taking into consideration the ship size
    elif playerX >= 736:
        playerX = 736


    # Enemy Movement

    for i in range(num_of_enemies):
        # game over
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                # get the enemy to go to y 2000
                enemyY[j] = 2000
            game_over_text()
            break
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 2
            enemyY[i] += enemyY_change[i]
            # 736 taking into consideration the ship size
        elif enemyX[i] >= 736:
            enemyX_change[i] = -2
            enemyY[i] += enemyY_change[i]
            # collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(2, 735)
            enemyY[i] = random.randint(50, 150)
            print(score_value)

        enemies(enemyX[i], enemyY[i], i)

    # bullet movement
    if bulletY <= 0:  # negative number
        bulletY = 480
        bullet_state = "ready"
    # we change the state so we can control the bullet and fire again

    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change
# this is running inside the while loop
    player(playerX, playerY)
    sow_score(textX, textY)

    # to update the screen | so that everything happen in game is updating
    pygame.display.update()
