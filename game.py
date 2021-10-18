import pygame
from comet_event import CometEvent
from player import Player
from monster import Monster
from random import randint


class Game:

    def __init__(self):
        self.is_playing = False
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        self.all_monsters = pygame.sprite.Group()
        self.spawn_monster()
        self.spawn_monster()
        self.comet_fall = CometEvent(self)

    def start_game(self):
        self.is_playing = True
        self.spawn_rand_monster()

    def game_over(self):
        self.all_monsters = pygame.sprite.Group()
        self.comet_fall.all_comets = pygame.sprite.Group()
        self.comet_fall.reset_percent()
        self.player.health = 100
        self.is_playing = False

    def update_game(self, screen):
        # appliquer l'image du joueur
        screen.blit(self.player.image, self.player.rect)

        # Dessin barre de vie
        self.player.max_health_bar(screen)
        self.player.update_health_bar(screen)

        # Barre event
        self.comet_fall.update_bar(screen)
        # Projectiles UwU
        for projectile in self.player.all_projectiles:
            projectile.move()
            if projectile.rect.x > 1080:
                projectile.player.all_projectiles.remove(projectile)

        # Dessin monstre
        self.all_monsters.draw(screen)
        for monster in self.all_monsters:
            monster.forward()
            monster.max_health_bar(screen)
            monster.update_health_bar(screen)

        # Dessin comete
        self.comet_fall.all_comets.draw(screen)
        for comet in self.comet_fall.all_comets:
            comet.fall()

        # Dessin projectiles
        self.player.all_projectiles.draw(screen)

        if 0 < self.player.rect.x < 1080 - self.player.rect.width:
            self.player.move()
        elif self.player.rect.x == 0:
            self.player.rect.x += 2
        elif self.player.rect.x == 1080 - self.player.rect.width:
            self.player.rect.x -= 2

    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(
            sprite, group, False, pygame.sprite.collide_mask)

    def spawn_rand_monster(self):
        for x in range(randint(2, 3)):
            self.spawn_monster()
