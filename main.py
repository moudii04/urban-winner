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

# Charger la bannier
banner = pygame.image.load("C:/Users/EM/Desktop/tuto/assets/banner2.png")
banner_rect = banner.get_rect()
banner_rect.x = screen.get_width()//4 - 50
# Boutton de lancer
play_button = pygame.image.load("C:/Users/EM/Desktop/tuto/assets/button.png")
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = screen.get_width()//3 - 30
play_button_rect.y = screen.get_height()/2 + 100

# Charger le jeu
game = Game()


launched = True
while launched:
    # appliquer le background
    screen.blit(bg, (0, -200))

    if game.is_playing:
        game.update_game(screen)
    else:

        # appilquer la banner
        screen.blit(banner, banner_rect)

        # appliquer le bouton
        screen.blit(play_button, (play_button_rect))

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

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play_button_rect.collidepoint(event.pos):
                game.start_game()

        if event.type == pygame.QUIT:
            launched = False
