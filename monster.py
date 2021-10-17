import pygame
import random


class Monster(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 50
        self.velocity = 1
        self.max_health = 100
        self.attack = 0.5
        self.image = pygame.image.load("assets/mummy.png")
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 540

    def damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.rect.x = 1000 + random.randint(0, 300)
            self.health = 100

    def update_health_bar(self, surface):

        pygame.draw.rect(surface, (50, 255, 70), [
                         self.rect.x + 10, self.rect.y - 15, self.health, 5])

    def max_health_bar(self, surface):

        pygame.draw.rect(surface, (60, 60, 60), [
                         self.rect.x + 10, self.rect.y - 15, self.max_health, 5])

    def forward(self):
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        else:
            self.game.player.damage(self.attack)
