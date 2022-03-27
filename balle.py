import pygame
import time
class Balle(pygame.sprite.Sprite): #Il s'agit de la balle tirée par la lunette de visée (avec espace)
    def __init__(self, joueur):
        super().__init__()
        self.velocity = 10
        self.image = pygame.image.load("images/point_rouge.png")
        self.image = pygame.transform.scale(self.image, (30, 22))
        self.joueur = joueur
        self.rect = self.image.get_rect()
        self.rect.x = joueur.rect.x + 85
        self.rect.y = joueur.rect.y + 90
        global kill4
        kill4=0

    def remove(self):
        self.joueur.all_projectiles.remove(self)

    def remove_2(self):
        return

    def health_bar(self,surface):
        return

    def col2(self):
        return

    def col(self):
        global kill4
        for cactus in self.joueur.game.check_collision(self, self.joueur.game.all_monsters) or self.joueur.game.check_collision(self,self.joueur.game.cactus2.c2) or self.joueur.game.check_collision(self,self.joueur.game.cactus3.c3) or self.joueur.game.check_collision(self,self.joueur.game.cactus4.c4) or self.joueur.game.check_collision(self,self.joueur.game.cactus5.c5) :
            kill4+=1
            if kill4<2:
                cactus.damage(50) #50 dégats après collision
    def change(self, val):
        return

    def move_bas(self):
        return
    def avancer(self):
        return

    def avancer2(self,ar):
        return
    
    def dessin(self,ver,background):
        return
    def remove_3(self):
        return

    def damage(self, amount):
        return

    def remplis(self):
        return

    def health(self):
        a = self.health
        return a


class Balle_2(pygame.sprite.Sprite): #Il s'agit du fusil à pompe
    def __init__(self, joueur):
        super().__init__()
        self.velocity = 10
        self.image = pygame.image.load("images/point_rouge.png").convert_alpha()
        #self.image2 = pygame.image.load("images/point_rouge.png")
        #self.image2 = pygame.transform.scale(self.image, (700, 500))
        self.image = pygame.transform.scale(self.image, (700, 500))
        self.joueur = joueur
        self.rect = self.image.get_rect()
        self.rect.x = joueur.rect.x - 255
        self.rect.y = joueur.rect.y - 120
        global kill3
        kill3 = 0

    def change(self, val):
        return

    def health_bar(self,surface):
        return

    def col2(self):
        return

    def remove(self):
        #self.joueur.all_projectiles.remove(self)
        return
    def remove_2(self):
        self.joueur.all_projectiles.remove(self)
    def remove_3(self):
        return
    def col(self):
        global kill3
        for cactus in self.joueur.game.check_collision(self, self.joueur.game.all_monsters) or self.joueur.game.check_collision(self,self.joueur.game.cactus2.c2) or self.joueur.game.check_collision(self,self.joueur.game.cactus3.c3) or self.joueur.game.check_collision(self,self.joueur.game.cactus3.c3) or self.joueur.game.check_collision(self,self.joueur.game.cactus4.c4) or self.joueur.game.check_collision(self,self.joueur.game.cactus5.c5) :
            kill3+=1
            if kill3==1 and cactus.get_vagg5()>=1:
                break
            if kill3<3:
                cactus.damage(500)



    def move_bas(self):
        return
    def avancer(self):
        return
    def avancer2(self,ar):
        return
    
    def dessin(self,ver,background):
        return

    def damage(self, amount):
        return

    def remplis(self):
        return

    def health(self):
        a = self.health
        return a




