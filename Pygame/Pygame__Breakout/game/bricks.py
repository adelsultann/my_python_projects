import pygame
from game.constants import Constants

bricks = [
    "assets/element_blue_rectangle.png",
    "assets/element_green_rectangle.png",
    "assets/element_grey_rectangle.png",
    "assets/element_purple_rectangle.png",
    "assets/element_red_rectangle.png",
    "assets/element_yellow_rectangle.png",
]


class Bricks():
    def __init__(self, all_sprites):
        self.all_sprites = all_sprites
        self.all_bricks = pygame.sprite.Group()

        for r in range(Constants.brick_rows):
            for c in range(Constants.brick_cols):
                brick = Brick(r, c)
                self.all_sprites.add(brick)
                self.all_bricks.add(brick)


    def check_collisions(self,ball):
        collision_list = pygame.sprite.spritecollide(ball,self.all_bricks,False)
        for brick in collision_list:
            ball.bounce()
            brick.kill()

# we first work on the sprite then we did the class above to loop through the Sprite
class Brick(pygame.sprite.Sprite):
    def __init__(self, row, col):
        super().__init__()
        self.x_pos = col * 90 + 35
        self.y_pos = row * 40 + 30
        self.image = pygame.image.load((bricks[row]))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x_pos, self.y_pos)
