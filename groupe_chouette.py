import pygame
from chouette import *
class groupe_arbre(pygame.sprite.Sprite):
    def __init__(self,game):
        super().__init__()
        self.arbre = pygame.sprite.Group()

    def launch_arbre(self):
        self.arbre.add(Arbre(self))


class groupe_chouette(pygame.sprite.Sprite):
    def __init__(self,game):
        super().__init__()
        self.chouette = pygame.sprite.Group()
    def launch_chouette(self):
        self.chouette.add(Chouette(self))



