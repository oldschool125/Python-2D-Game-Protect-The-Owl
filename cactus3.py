import pygame
from cactus import *
class groupe_3(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.c3 = pygame.sprite.Group()

    def launch_c3(self):
        self.c3.add(Cactus3(self))