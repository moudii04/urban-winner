import pygame
from random import randint


class Comet(pygame.sprite.Sprite):

    def __init__(self, comet_event):
        super().__init__()
        self.image = pygame.image.load(
            "C:/Users/EM/Desktop/tuto/assets/comet.png")
        self.rect = self.image.get_rect()
        self.velocity = randint(2, 4)
        self.rect.x = randint(20, 900)
        self.rect.y = -randint(0, 300)
        self.comet_event = comet_event
        self.attack = 15

    def remove(self):
        self.comet_event.all_comets.remove(self)

    def fall(self):
        self.rect.y += self.velocity
        if self.rect.y >= 600:
            self.remove()
            self.comet_event.game.sound.play("meteorite")

        if len(self.comet_event.all_comets) == 0:
            self.comet_event.reset_percent()
            self.comet_event.fall_mode = False

        if self.comet_event.game.check_collision(self, self.comet_event.game.all_players):
            self.comet_event.game.player.damage(self.attack)
            self.remove()
