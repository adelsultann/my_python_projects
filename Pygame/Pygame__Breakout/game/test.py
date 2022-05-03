import pygame
import sys
from random import randint

bricks = [
    "assets/element_blue_rectangle.png",
    "assets/element_green_rectangle.png",
    "assets/element_grey_rectangle.png",
    "assets/element_purple_rectangle.png",
    "assets/element_red_rectangle.png",
    "assets/element_yellow_rectangle.png",
]
pygame.init()
width = 800
height = 600

screen = pygame.display.set_mode((width, height))


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x_pos = width / 2
        self.y_pos = height / 2
        self.image = pygame.image.load("ballBlue.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.velocity = [1, 1]
        self.rect.center = (self.x_pos, self.y_pos)

    def update(self):

        self.x_pos += self.velocity[0]
        self.y_pos += self.velocity[1]
        self.rect.center = (self.x_pos, self.y_pos)
        if self.x_pos < 11 or self.x_pos > width:
            self.velocity[0] = - self.velocity[0]
            self.rect.center = (self.x_pos, self.y_pos)
        if self.y_pos < 11 or self.y_pos > height:
            self.velocity[1] = randint(-4, 4)
            self.rect.center = (self.x_pos, self.y_pos)


ball = Ball()

ball_group = pygame.sprite.Group()
ball_group.add(ball)

brick_color = (250, 50, 0)
bricks = []

for row in range(3):
    for col in range(10):
        brick = pygame.Rect(col * 80 + 10, row * 40 + 60, 60, 20)
        bricks.append(brick)

run = True

r = pygame.Rect(0 * 80 + 10, 0 * 40 + 60, 60, 20)





while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
    screen.fill("Black")

    pygame.draw.rect(screen, "white", r)

    ball_group.update()
    ball_group.draw(screen)

    for brick in bricks:
        pygame.draw.rect(screen, brick_color, brick)

    pygame.display.update()
