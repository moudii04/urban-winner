import pygame
from pygame import image
from pygame.constants import K_SPACE
from game import Game

pygame.init()

i = 0
# Generer la fenetre
a = 1080
b = 720

arial_font = pygame.font.SysFont("arial", 20)
white_color = (255, 255, 255)


resolution = (a, b)
pygame.display.set_caption("Tutoriel")
screen = pygame.display.set_mode(resolution, pygame.RESIZABLE)

# Charger le background
bg = pygame.image.load("C:/Users/EM/Desktop/tuto/assets/back.jpg")

# Charger le jeu
game = Game()


launched = True
while launched:
    # appliquer le background
    screen.blit(bg, (0, -200))

    # appliquer l'image du joueur
    screen.blit(game.player.image, game.player.rect)

    # Dessin barre de vie
    game.player.max_health_bar(screen)
    game.player.update_health_bar(screen)

    # Projectiles UwU
    for projectile in game.player.all_projectiles:
        projectile.move()
        if projectile.rect.x > a:
            projectile.player.all_projectiles.remove(projectile)

    # Dessin monstre
    game.all_monsters.draw(screen)
    for monster in game.all_monsters:
        monster.forward()
        monster.max_health_bar(screen)
        monster.update_health_bar(screen)

    # Dessin projectiles
    game.player.all_projectiles.draw(screen)

    if 0 < game.player.rect.x < a - game.player.rect.width:
        game.player.move()
    elif game.player.rect.x == 0:
        game.player.rect.x += 2
    elif game.player.rect.x == a - game.player.rect.width:
        game.player.rect.x -= 2

    # Flip
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.VIDEORESIZE:
            a = int("{}".format(event.w))
            b = int("{}".format(event.h))
            game.player.velocity = a//700

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()
                i += 1

        if event.type == pygame.QUIT:
            launched = False
