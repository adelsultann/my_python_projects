import pygame
from game.constants import Constants


class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = Constants.screen_width / 2, Constants.screen_height / 2
        self.run_display = True
        # the arguments of Rect is (width,height,left,top,) or
        self.cursor_rect = pygame.Rect(0, 0, 60, 20)
        self.offset = - 100

    def draw_cursor(self):
        self.game.draw_text("*", 15, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        # blit the menu screen in the game class
        self.game.screen.blit(self.game.screen, (0, 0))
        pygame.display.update()
        # after we press keydown on the keyboard we rest the key to false so we don't
        # get glitch
        self.game.reset_keys()


class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Start"
        # the position of the start option in the menu
        self.startx, self.starty = self.mid_w, self.mid_h + 30
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + 50
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.handle_events()
            self.check_input()
            self.game.screen.fill(self.game.BLACK)
            # to draw = write the menu we use the draw_text function in the game class
            self.game.draw_text('Main Menu', 20, Constants.screen_width / 2, Constants.screen_height / 2 - 20)
            self.game.draw_text("Start Game", 20, self.startx, self.starty)
            self.game.draw_text("Credits", 20, self.creditsx, self.creditsy)
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
        elif self.game.UP_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'

            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'

    def check_input(self):
        self.move_cursor()
        # START_KEY is Enter in the keyboard
        if self.game.START_KEY:
            if self.state == 'Start':
                self.game.playing = True

            elif self.state == 'Credits':
                self.game.curr_menu = self.game.credits
        self.run_display = False


class CreditsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.handle_events()
            # get back to the main menu when the user press back button
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.screen.fill(self.game.BLACK)
            self.game.draw_text('Credits', 20, Constants.screen_width / 2, Constants.screen_height / 2 - 20)
            self.game.draw_text('Made by Adel', 15, Constants.screen_width / 2, Constants.screen_height / 2 + 10)
            self.blit_screen()
