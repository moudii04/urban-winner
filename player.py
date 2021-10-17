import pygame
from monster import Monster
from pro import Projectile


class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100.4
        self.max_health = 100
        self.attack = 10
        self.velocity = 2
        self.image = pygame.image.load(
            "C:/Users/EM/Desktop/tuto/assets/player.png")
        self.rect = self.image.get_rect()
        self.rect.x = 360
        self.rect.y = 500
        self.all_projectiles = pygame.sprite.Group()

    def launch_projectile(self):
        self.all_projectiles.add(Projectile(self))

    def move(self):
        keys = pygame.key.get_pressed()

        """if keys[pygame.K_UP]:
            self.rect.y -= 1
        elif keys[pygame.K_DOWN]:
            self.rect.y += 1"""

        if keys[pygame.K_LEFT] or keys[pygame.K_q]:
            self.rect.x -= self.velocity

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if not self.game.check_collision(self, self.game.all_monsters):
                self.rect.x += self.velocity

    def stop(self):
        if self.rect.x < 5:
            self.rect.x = self.rect.x+1
        elif self.rect.x == 1920:
            self.rect.x = 1919

    def update_health_bar(self, surface):

        pygame.draw.rect(surface, (50, 255, 70), [
                         self.rect.x + 50, self.rect.y + 20, self.health, 5])

    def max_health_bar(self, surface):

        pygame.draw.rect(surface, (60, 60, 60), [
            self.rect.x + 50, self.rect.y + 20, self.max_health, 5])

    def damage(self, amount):
        if self.health > amount:
            self.health -= amount
