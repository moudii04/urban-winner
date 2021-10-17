import pygame
from pygame import sprite
from player import Player
from monster import Monster


class Game:

    def __init__(self):
        self.is_playing = True
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        self.all_monsters = pygame.sprite.Group()
        self.spawn_monster()
        self.spawn_monster()

    def update_game(self, screen):
        # appliquer l'image du joueur
        screen.blit(self.player.image, self.player.rect)

        # Dessin barre de vie
        self.player.max_health_bar(screen)
        self.player.update_health_bar(screen)

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
