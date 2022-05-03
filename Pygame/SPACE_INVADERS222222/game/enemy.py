import random
import math
import pygame
from random import randint
from game.constants import Constants


class Enemies():
    def __init__(self, all_sprites):
        self.enemy_number = Constants.enemy_number
        self.all_sprites = all_sprites
        self.all_enemies = pygame.sprite.Group()

        self.score = 0
        self.lives = 3

        # for r in range(self.enemy_count):
        #     self.enemy_count += 2
        #     pos_x = random.randint(1, Constants.screen_width)
        #     # will increase this number so the enemy come down to the player in the Enemy class
        #     pos_y = 100
        #     one_enemy = Enemy("assets/enemy.png", pos_x, pos_y)
        #     self.all_enemies.add(one_enemy)
        #     self.all_sprites.add(one_enemy)

    def create_enemy(self):
        for enemy in range(self.enemy_number):
            pos_x = random.randint(1, Constants.screen_width)
            pos_y = random.randint(0, 300)
            one_enemy = Enemy("assets/enemy.png", pos_x, pos_y)
            self.all_enemies.add(one_enemy)
            self.all_sprites.add(one_enemy)
            self.enemy_number += 1
            Constants.enemy_speed += 00.2
            if self.enemy_number <= 7:
                self.enemy_number = 5

    def check_enemy(self):
        # if not self.all_enemies:
        #     print("no enemies")
        return self.all_enemies

    def check_collisions_with_player(self, player):
        collision_list = pygame.sprite.spritecollide(player, self.all_enemies, False)
        for enemy in collision_list:
            enemy.kill()
            self.lives -= 1

    def check_collisions(self, bullet):
        collision_list = pygame.sprite.spritecollide(bullet, self.all_enemies, False)
        for enemy in collision_list:
            enemy.kill()
            self.score += 1


class Enemy(pygame.sprite.Sprite):
    def __init__(self, picture_path, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)
        self.enemyX_change = Constants.enemy_speed
        self.enemyY_change = Constants.enemyY_change

    def update(self):
        # let's see we started self.rect.x = 200 | 200 + 4 = 204
        # let's we reach the right wall then we have 700| 700 - 4 = 696
        # 5 = 5 + 0.1
        self.rect.x += self.enemyX_change
        if self.rect.x <= 0:
            self.enemyX_change = Constants.enemy_speed  # we can increase the speed if you want
            self.rect.y += self.enemyY_change
        elif self.rect.x >= 740:
            self.enemyX_change = -Constants.enemy_speed
            self.rect.y += self.enemyY_change
