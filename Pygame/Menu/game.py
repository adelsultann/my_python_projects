import pygame
from menu import *
from random import randint
from menu import *

class Game():
    def __init__(self):
        pygame.init()
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.DISPLAY_W, self.DISPLAY_H = 480, 270
        self.display = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H))
        self.window = pygame.display.set_mode(((self.DISPLAY_W, self.DISPLAY_H)))
        self.font_name = '8-BIT WONDER.TTF'
        # self.font_name = pygame.font.get_default_font()
        self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255)
        # the Game class will pass itself in this case
        self.main_menu = MainMenu(self)
        self.options = OptionsMenu(self)
        self.credits = CreditsMenu(self)
        self.curr_menu = self.main_menu
    def game_loop(self):
        while self.playing:
            self.check_events()
            if self.START_KEY:
                self.playing = False
            self.display.fill(self.BLACK)
            self.draw_ball()
            self.draw_text('Thanks for Playing', 20, self.DISPLAY_W/2, self.DISPLAY_H/2)
            self.window.blit(self.display, (0, 0))
            pygame.display.update()
            self.reset_keys()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True

    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

    def draw_ball(self):
        # the ball doesn't move because we go back to the same position each loop
        self.image = pygame.image.load("ballBlue.png")
        self.rect = self.image.get_rect()
        self.x_pos = self.DISPLAY_W / 2
        self.y_pos = self.DISPLAY_H / 2
        self.velocity = [randint(2, 4), randint(-4, 4)]
        self.rect.center = (self.x_pos, self.y_pos)
        self.update(self.x_pos, self.y_pos)
        self.display.blit(self.image, self.rect.center)

    def update(self, x_pos, y_pos):
        # if x_pos < 0 or x_pos > self.DISPLAY_W - 11:
        #     self.velocity[0] = -self.velocity[0]
        # if y_pos < 0:
        #     self.velocity[1] = -self.velocity[1]
        #
        # if self.velocity[0] == 0:
        #     self.velocity[0] += 1
        # if self.velocity[1] == 0:
        #     self.velocity[1] += 1

        x_pos += self.velocity[0]
        y_pos += self.velocity[1]
        self.rect.center = (x_pos, y_pos)

    def draw_text(self, text, size, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_surface, text_rect)