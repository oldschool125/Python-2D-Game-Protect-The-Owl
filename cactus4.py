import pygame
from cactus import *
class groupe_4(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.c4 = pygame.sprite.Group()

    def launch_c4(self):
        self.c4.add(Cactus4(self))