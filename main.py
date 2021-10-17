import pygame
from pygame.display import update
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

    if game.is_playing:
        game.update_game(screen)

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
