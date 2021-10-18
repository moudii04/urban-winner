from random import randint
import pygame
from comet import Comet


class CometEvent():

    def __init__(self, game):
        self.percent = 0
        self.percent_speed = 0.075
        self.all_comets = pygame.sprite.Group()
        self.game = game
        self.fall_mode = False

    def add_percent(self):
        self.percent += self.percent_speed

    def full_loaded(self):
        return self.percent >= 100

    def reset_percent(self):
        self.fall_mode = False
        self.percent = 0
        self.game.spawn_rand_monster()

    def meteor_fall(self):
        for x in range(randint(10, 12)):
            self.all_comets.add(Comet(self))

    def attempt_fall(self):
        if self.full_loaded() and len(self.game.all_monsters) == 0:
            self.fall_mode = True
            self.meteor_fall()

    def update_bar(self, surface):

        self.add_percent()

        pygame.draw.rect(surface, (0, 0, 0), [0,
                                              surface.get_height()-20, surface.get_width(), 10])
        pygame.draw.rect(surface, (187, 11, 10), [
                         0, surface.get_height() - 20, (surface.get_width()/100)*self.percent, 10])
