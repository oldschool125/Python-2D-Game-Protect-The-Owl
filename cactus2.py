import pygame
from cactus import *

#Création de groupes pour chaque cactus (le premier cactus est dans game.all_monsters, le deuxieme dans c2, ...)
class groupe_2(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.c2 = pygame.sprite.Group()

    def launch_c2(self):
        self.c2.add(Cactus2(self))

