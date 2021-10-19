import pygame


class SoundManager:

    def __init__(self):
        self.sounds = {
            "click": pygame.mixer.Sound("C:/Users/EM/Desktop/tuto/assets/sounds/click.ogg"),
            "end": pygame.mixer.Sound("C:/Users/EM/Desktop/tuto/assets/sounds/end.ogg"),
            "meteorite": pygame.mixer.Sound("C:/Users/EM/Desktop/tuto/assets/sounds/meteorite.ogg"),
            "tir": pygame.mixer.Sound("C:/Users/EM/Desktop/tuto/assets/sounds/tir.ogg"),
        }

    def play(self, sound_name):
        self.sounds[sound_name].play()
