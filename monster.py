import pygame
import random
import animation


class Monster(animation.AnimationSprite):
    def __init__(self, game, name):
        super().__init__(name)
        self.game = game
        self.health = 100
        self.velocity = 1
        self.max_health = 100
        self.attack = 0.5
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 540
        self.start_animation()

    def damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.rect.x = 1000 + random.randint(0, 300)
            self.health = self.max_health
            self.game.add_score(20)

        if self.game.comet_fall.full_loaded():
            self.game.all_monsters.remove(self)
            self.game.comet_fall.attempt_fall()

    def update_animation(self):
        self.animate(loop=True)

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


class Mummy(Monster):
    def __init__(self, game):
        super().__init__(game, "mummy")


"""class Alien(Monster):
    def __init__(self, game):
        super().__init__(game, "alien")"""
