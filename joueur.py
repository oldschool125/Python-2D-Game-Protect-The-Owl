import pygame
from balle import *
from meteorite import Meteorite
from meteorite import Bomb
from cactus_allie import Allie
from epines import *
from cactus import Cactus
from bouclier import Bouclier

#classe représentant le joueur
class Player(pygame.sprite.Sprite):
#Un sprite, ou lutin, est dans le jeu vidéo un élément graphique qui peut se déplacer sur l'écran.

    def __init__(self, game):
        super().__init__()
        # les attaques infligés par les balles
        self.attack = 100
        # velocité des déplacements du joueur
        # dans notre cas ne se déplace pas
        self.game = game
        self.velocity = 1.7
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load('images/lun.png')
        self.image = pygame.transform.scale(self.image, (200, 200))
        #cree une carré pour recuperer l'image et la déplacer
        self.rect = self.image.get_rect()
        #les coordonnées servent à le placer au centre
        self.rect.x = 500
        self.rect.y = 300

    def launch_balle(self):
        self.all_projectiles.add(Balle(self))
    def launch_balle_2(self):
        self.all_projectiles.add(Balle_2(self))
    def launch_meteorite(self):
        self.all_projectiles.add(Meteorite(self))
    def launch_bomb(self):
        self.all_projectiles.add(Bomb(self))

    def launch_cactus(self):
        self.all_projectiles.add(Allie(self))
    def move_right(self):
        self.rect.x += self.velocity
    def position_2(self):
        a,b=Cactus.position_2(self)
        return a,b

    def move_left(self):
        self.rect.x -= self.velocity
    def position_2_2(self):
        a,b=Cactus2.position_2(self)
        return a,b
    def move_up(self):
        self.rect.y -= self.velocity
    def position_2_5(self):
        a,b=Cactus5.position_2(self)
        return a,b
    def position_2_3(self):
        a,b=Cactus3.position_2(self)
        return a,b

    def move_down(self):
        self.rect.y += self.velocity
    def position_2_4(self):
        a,b=Cactus4.position_2(self)
        return a,b
        
    def launch_epine(self):
        self.all_projectiles.add(Epines(self))
    def launch_epine2(self):
        self.all_projectiles.add(Epines2(self))
    def launch_epine3(self):
        self.all_projectiles.add(Epines3(self))
    def launch_epine4(self):
        self.all_projectiles.add(Epines4(self))
    def launch_epine5(self):
        self.all_projectiles.add(Epines5(self))
    def launch_bouclier(self):
        self.all_projectiles.add(Bouclier(self))