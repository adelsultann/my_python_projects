import pygame
import sys
from game.player import Player
from game.constants import Constants
from game.bullet import Bullet
from game.enemy import Enemies
from game.menu import *

class Game():
    def __init__(self):
        pygame.init()
        self.running, self.playing = True,False
        self.display = pygame.Surface((Constants.screen_width, Constants.screen_height))
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

        self.screen = pygame.display.set_mode(size=(Constants.screen_width, Constants.screen_height))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("MY GAME")
        self.bg_color = pygame.Color("black")
        self.font = pygame.font.Font("assets/Kenney_Future.ttf", 20)

        self.font_name = 'assets/8-BIT WONDER.TTF'
        self.game_over = False
        self.bg_img = pygame.image.load("assets/background.png")
        self.bg_img = pygame.transform.scale(self.bg_img, (Constants.screen_width, Constants.screen_height))
        self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255)
        self.main_menu = MainMenu(self)
        self.credits = CreditsMenu(self)
        self.curr_menu = self.main_menu

        self.player = Player()
        self.bullet = Bullet()

        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player, self.bullet)
        self.enemy = Enemies(self.all_sprites)


    def update(self):
        # check_enemy function check if there are enemy in the game
        # if yes return True

        if not self.enemy.check_enemy():
            self.enemy.create_enemy()
        self.enemy.check_collisions(self.bullet)

        self.enemy.check_collisions_with_player(self.player)
        if self.enemy.lives <= 0:
            self.game_over = True
        self.all_sprites.update()


        pygame.display.update()
        self.reset_keys()
        self.clock.tick(120)

    def draw(self):
        self.screen.fill((0, 0, 0))
        if self.game_over:
            text1 = self.font.render("Game Over!", True, "white")
            self.screen.blit(text1, (Constants.screen_width / 2 - 70, Constants.screen_height / 2))
        else:

            self.screen.blit(self.bg_img, (0, 0))
            self.all_sprites.draw(self.screen)
            text = self.font.render(f"Score: {self.enemy.score}", True, "white")
            self.screen.blit(text, (25, Constants.screen_height - 30))
            text1 = self.font.render(f"Lives: {self.enemy.lives}", True, "white")
            self.screen.blit(text1, (700, Constants.screen_height - 30))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player.move(Constants.player_speed)
        if keys[pygame.K_RIGHT]:
            self.player.move(-Constants.player_speed)

        if keys[pygame.K_SPACE]:
            if self.bullet.bullet_state is "ready":
                # we add to the x position 15 pixel so the bullet fire from
                # the middle of the rocket
                self.bullet.rect.x = self.player.rect.x + 15
                self.bullet.rect.y = self.player.rect.y







    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

    def draw_text(self, text, size, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, (self.WHITE))
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.screen.blit(text_surface, text_rect)