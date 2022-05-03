import sys, pygame
import random
pygame.init()

size = width, height = 800, 400

speed = [1, 1]

background = 255, 255, 255

screen = pygame.display.set_mode(size)

pygame.display.set_caption("Bouncing ball")

ball = pygame.image.load("football.png")



ballrect = ball.get_rect()

RUNNING = True
while RUNNING:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            sys.exit()

    ballrect = ballrect.move(speed)

    if ballrect.left < 0 or ballrect.right > width:
        print(ballrect)

        speed[0] = -speed[0]
        print(speed[0])

    if ballrect.top < 0 or ballrect.bottom > height:

        speed[1] = -speed[1]

    screen.fill(background)

    screen.blit(ball,ballrect
                )

    pygame.display.flip()