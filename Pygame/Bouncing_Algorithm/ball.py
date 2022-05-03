import pygame
import random
BLACK = (0, 0, 0)


class Ball(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        # surfaces are generally used to represent the
        # appearance of the object and its position on the screen
        # Pass in the color of the ball, its width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        # draw the ball
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # the speed
        self.velocity = [random.randint(4, 8), random.randint(-8, 8)]

        # fetch the ball object with the dimension of the image
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        if self.rect.y >= 200:
            self.velocity[1] = -self.velocity[1]
