import pygame
from game.constants import Constants


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/player.png").convert_alpha()
        self.rect = self.image.get_rect()
        # the position of the player
        self.x_pos = Constants.screen_width / 2
        self.y_pos = Constants.screen_height - 50
        self.rect.center = (self.x_pos, self.y_pos)
        self.lives = Constants.starting_lives




    def move(self, pixel):
        self.x_pos -= pixel
        # check if the player hit the wall
        if self.x_pos < 30:
            self.x_pos = 30
        elif self.x_pos >= 765:
            self.x_pos = 765
        self.rect.center = (self.x_pos, self.y_pos)




