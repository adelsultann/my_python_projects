import pygame
from game.constants import Constants



class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # صار الصاروخ يطلع في بدايه اللعبه عشان كذا حطيت الرقم هذا بحيث يكون خارج اللعبه ثم يتم التحكم به لاحقا
        # self.x_pos = 900
        # self.y_pos = Constants.screen_height / 2
        self.image = pygame.image.load("assets/bullet.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.bulletY_change = -3
        self.bullet_state = "ready"
        #self.rect.center = (self.x_pos, self.y_pos)





    def update(self):
        self.bullet_state = "fire"
        self.rect.y += self.bulletY_change
        if self.rect.y <= 0:
            self.bullet_state = "ready"


