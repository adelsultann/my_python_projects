import pygame
import math
import random
BLACK = (0, 0, 0)






class Enemy(pygame.sprite.Sprite):
    def __init__(self,picture_path,pos_x,pos_y):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x,pos_y]
        self.enemyX_change = 4
        self.enemyY_change = 40


    def update(self):
        # let's see we started self.rect.x = 200 | 200 + 4 = 204
        # let's we reach the right wall then we have 700| 700 - 4 = 696
        # 5 = 5 + 0.1
        self.rect.x += self.enemyX_change
        if self.rect.x <= 0:
            self.enemyX_change = 4 # we can increase the speed if you want
            self.rect.y += self.enemyY_change
        elif self.rect.x >= 740:
            self.enemyX_change = -4
            self.rect.y += self.enemyY_change





class Bullet(pygame.sprite.Sprite):
    def __init__(self,picture_path):
        super().__init__()
        self.image = pygame.image.load(picture_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.bulletY_change = -3
        self.bullet_state = "ready"



    def update(self):
        self.bullet_state = "fire"
        self.rect.y += self.bulletY_change
        if self.rect.y <= 0:
            self.bullet_state = "ready"






class Invader(pygame.sprite.Sprite):
    def __init__(self, picture_path):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()


    def move_right(self, pixel):

        self.rect.x -= pixel
        # Check that you are not going too far (off the screen)
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x >= 740:
            self.rect.x = 740





def isCollision(enemyX, enemyY, bulletX, bulletY):
    # this is equation for the distance
    # https://www.mathplanet.com/education/algebra-2/conic-sections/distance-between-two-points-and-the-midpoint
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY, 2))
    # we come with 27 after trying and when we want to consider collision
    if distance < 27:
        return True
    else:
        return False
