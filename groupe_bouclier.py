import pygame
from bouclier import *
class groupe_bouclier(pygame.sprite.Sprite):
    def __init__(self,game):
        super().__init__()
        self.bouclier = pygame.sprite.Group()

    def launch_bouclier(self):
        self.bouclier.add(Bouclier(self))
