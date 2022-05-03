import pygame

WHITE = (255, 255, 255)


class Crosshair(pygame.sprite.Sprite):

    def __init__(self, picture_path):
        super().__init__()
        # this is blank imag at this moment
        self.image = pygame.image.load(picture_path)
        # fill it with color
        # self.image.fill(color)
        # this method is to draw rectangle around the picture so you can control it
        self.rect = self.image.get_rect()
        # update is very specific method that predefined in the sprite class
        self.gunshot_sound = pygame.mixer.Sound("sounds/glock19-18535.wav")


    def update(self):
        # to make the position follow the mouse corsair
        self.rect.center = pygame.mouse.get_pos()

    def shoot_sound(self):
        self.gunshot_sound.play()





class Target(pygame.sprite.Sprite):
    def __init__(self, picture_path, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        # fill it with color
        # self.image.fill(color)
        # this method is to draw rectangle around the picture so you can control it
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]
