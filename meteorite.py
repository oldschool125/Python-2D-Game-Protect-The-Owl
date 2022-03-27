import pygame
from cactus2 import *
from cactus3 import *
from cactus4 import *
from cactus5 import *
class Meteorite(pygame.sprite.Sprite): #Il s'agit du missile géant (avec T)
    def __init__(self, joueur):
        super().__init__()
        self.velocity = 10
        self.image = pygame.image.load("images/missilev1.png")
        self.image = pygame.transform.scale(self.image, (700,850))
        self.image = pygame.transform.rotate(self.image,-50)
        self.joueur = joueur
        self.rect = self.image.get_rect()
        self.rect.x = -1200
        self.rect.y = -180
        global killm
        killm=0
    def change(self, val):
        return
    def col2(self):
        return

    def health_bar(self,surface):
        return
    def col(self):
        global killm
        for cactus in self.joueur.game.check_collision(self, self.joueur.game.all_monsters) or self.joueur.game.check_collision(self,self.joueur.game.cactus2.c2) or self.joueur.game.check_collision(self,self.joueur.game.cactus3.c3) or self.joueur.game.check_collision(self,self.joueur.game.cactus3.c3) or self.joueur.game.check_collision(self,self.joueur.game.cactus4.c4) or self.joueur.game.check_collision(self,self.joueur.game.cactus5.c5) :
            if cactus.get_vagg5()>=1 and killm>=1:
                #Pour ne pas tuer le boss directement
                break
            #One shot chaque cactus
            cactus.damage(1000)
            killm+=1

    def move_bas(self):
        global ver
        #Il bouge de la gauche vers la droite
        self.rect.x += 5*self.velocity
        self.rect.y += 100*self.velocity
        for i in range(100):
            continue
        self.rect.y -= 100*self.velocity
        if self.rect.x > 1180 :
            #Pour le faire disparaitre une fois sorti de l'écran
            self.joueur.all_projectiles.remove(self)
            for cactus in self.joueur.game.all_monsters:
                cactus.modif_compteur(0)
            for cactus in self.joueur.game.all_monsters:
                ver=True
                self.joueur.game.cactus.zero(self.joueur.game.cactus, ver)
                fait=1
    def avancer2(self,ar):
        return
    def remove(self):
        return
    def remove_2(self):
        return

    def remove_3(self):
        return

    def avancer(self):
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
class Bomb(pygame.sprite.Sprite): #Il s'agit du missile lancé avec E
    def __init__(self, joueur):
        super().__init__()
        self.velocity = 10
        self.image = pygame.image.load("images/bomb.png")
        self.image = pygame.transform.scale(self.image, (200,200))
        self.image = pygame.transform.rotate(self.image,35)
        self.joueur = joueur
        self.rect = self.image.get_rect()
        self.rect.x = joueur.rect.x
        self.rect.y = -490
        global kill2
        kill2=0
        self.cactus2 = groupe_2(self)
        self.cactus3 = groupe_3(self)
        self.cactus4 = groupe_4(self)
        self.cactus5 = groupe_5(self)

    def change(self, val):
        return
    def col2(self):
        return

    def health_bar(self,surface):
        return

    def col(self):

        global kill2
        for cactus in self.joueur.game.check_collision(self, self.joueur.game.all_monsters) or self.joueur.game.check_collision(self,self.joueur.game.cactus2.c2) or self.joueur.game.check_collision(self,self.joueur.game.cactus3.c3) or self.joueur.game.check_collision(self,self.joueur.game.cactus3.c3) or self.joueur.game.check_collision(self,self.joueur.game.cactus4.c4) or self.joueur.game.check_collision(self,self.joueur.game.cactus5.c5) :
            if kill2<2:
                # son quand l'utilsateur utilise l'attaque 'petit missile' (touche E)
                cactus.damage(500)
                pygame.init()
                pygame.mixer.pre_init()
                pygame.mixer.init()
                pygame.mixer.Channel(2).play(pygame.mixer.Sound('SONS/boom.wav'))
            kill2+=1
            if kill2==1 and cactus.get_vagg5()>=1:
                break
    def avancer2(self,ar):
        return

    def return_3(self):
        return

    def move_bas(self):
        global ver
        self.rect.y += 0.35*self.velocity
        if self.rect.y > 280 :
            #Dégats de zone quand le missile touche le sol
            for cactus in self.joueur.game.all_monsters :
                if cactus.get_vagg5()<1:
                    cactus.damage(cactus.max_health/3)
            for cactus2 in self.joueur.game.cactus2.c2:
                cactus2.damage(cactus2.max_health/3)
            for cactus3 in self.joueur.game.cactus3.c3:
                cactus3.damage(cactus3.max_health/3)
            for cactus4 in self.joueur.game.cactus4.c4:
                cactus4.damage(cactus4.max_health/3)
            for cactus5 in self.joueur.game.cactus5.c5:
                cactus5.damage(cactus5.max_health/3)
            self.joueur.all_projectiles.remove(self)

    def remove(self):
        return
    def remove_2(self):
        return
    def avancer(self,ar):
        return
    
    def dessin(self,ver,background):
        return

    def damage(self,amount):
        return

    def remplis(self):
        return

    def health(self):
        a = self.health
        return a
    



