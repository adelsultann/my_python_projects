import sys, pygame
import random
from ball import Ball
pygame.init()
DARK_BLUE = (36, 90, 190)

size = width, height = 800, 400

display = pygame.display.set_mode(size)
clock = pygame.time.Clock()
FPS = 60

acceleration = .5

# class Ball():
#     def __init__(self):
#         self.y = 90
#         self.velocity = 10
#
#     def draw(self):
#         pygame.draw.circle(display, (0, 0, 0), (400, int(self.y)), 15, 15)
#
#     def move(self):
#         self.velocity += acceleration
#         self.y += self.velocity
#         if self.y >= 200:
#             self.velocity = - self.velocity
all_sprites_list = pygame.sprite.Group()


ball = Ball(DARK_BLUE,10,10)
ball.rect.x = 300
ball.rect.y = 50
all_sprites_list.add(ball)


game = True

while game:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False


    display.fill((255, 255, 255))
    pygame.draw.line(display, DARK_BLUE, (0, 200), (800, 200), 3)
    # pygame.draw.circle(display, (0, 0, 0), (400, 90), 15, 15)
    # ball.draw()
    # ball.move()
    all_sprites_list.update()
    all_sprites_list.draw(display)
    pygame.display.update()
    clock.tick(FPS)
