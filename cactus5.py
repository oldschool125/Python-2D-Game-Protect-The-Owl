import pygame
from cactus import *
class groupe_5(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.c5 = pygame.sprite.Group()

    def launch_c5(self):
        self.c5.add(Cactus5(self))