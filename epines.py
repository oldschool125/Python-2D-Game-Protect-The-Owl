import pygame
from cactus import *

# 5 classes épines pour les 5 cactus ---> 1 classe par cactus ---> commentaires dans la 1ere classe
class Epines(pygame.sprite.Sprite):

    def __init__(self,joueur):
        super().__init__()
        self.velocity = 5
        self.joueur = joueur
        global mode
        mode = 0
        if mode == 0:
            self.image = pygame.image.load('images/epine_verte.png') # image de l'épine des cactus normaux
            self.image = pygame.transform.scale(self.image, (50, 50)) #réduire l'image
            # son quand les cactus lancent leurs épines
            pygame.init()
            pygame.mixer.pre_init()
            pygame.mixer.init()
            pygame.mixer.Channel(5).play(pygame.mixer.Sound('SONS/epine.wav'))
        self.rect= self.image.get_rect()
        a,b = self.joueur.position_2() #position x et y du cactus qui lance l'épine (a = x, b= y)
        if self.joueur.game.get_vag5()!=0:
            self.rect.x = a+200    #mettre l'épine au bon endroit
        else:
            self.rect.x=a
        self.rect.y=b
        self.stck = 600   #variable permettant de choisir le début de la courbe représentant la trajectoire
        global cptt
        global passe
        passe = 0
        cptt = 0
        global epnoir # épine du boss cactus
        epnoir = 0

    def health_bar(self,surface):
        return

    def damage(self, amount):
        return

    def remplis(self):
        return

    def health(self):
        a = self.health
        return a

    def col(self):
        global mode
        for chouette in self.joueur.game.check_collision(self,self.joueur.game.groupe_chouette.chouette) :
                if chouette.rect.x > -50 and self.joueur.game.get_bouclier() == 0: #si le bouclier n'est pas activé, la chouette va subir des dégats, sinon la condition ne sera pas lancé
                    chouette.damage(50) #degats subis par la chouette
                    self.joueur.all_projectiles.remove(self) #supprimer l'épine si elle touche la chouette
        a=500
        if self.joueur.game.get_vag5()!=0:
            a=450
        if self.rect.y>a:
            self.joueur.all_projectiles.remove(self) #Supprimer l'épine si elle touche le sol

    def col2(self):
        return

    def move_bas(self):
        return
    def avancer2(self,ar):
        return
    def change(self,val):
        self.rect.x=-200

    def remove(self):
        return
    def remove_3(self):
        if 1:
            self.joueur.all_projectiles.remove()
    def remove_2(self):
        return
    def avancer(self):
        return
    def dessin(self,ver,background):
        global cptt,mode, passe, epnoir
        if passe!=1:
            if ver == 1:
                self.image = pygame.image.load('images/epine_noire.png') #image de l'épine du boss
                self.image = pygame.transform.scale(self.image, (100, 100)) #mise à l'échelle du boss de l'épine noire
                if epnoir == 0 :
                    pygame.init()
                    pygame.mixer.pre_init()
                    pygame.mixer.init()
                    song = pygame.mixer.Sound('SONS/epine.wav') # son de l'épine
                    song.play()
                    epnoir += 1
            if cptt == 0:
                a, b = self.joueur.position_2()
                # print(a,b)
                if ver == 1:
                    self.rect.x = a + 200
                    self.rect.y = b

                    mode = 1
                else:
                    self.rect.x = a
                    self.rect.y = b

                cptt += 1
                # print('rentré')
                # print(self.rect.x,self.rect.y)
            self.rect.x = self.rect.x - 5 #faire bouger l'épine vers le gauche
            self.stck -= 5
            self.rect.y = int(0.0056 * self.stck * self.stck - 3.9709 * self.stck + 791.005) #polynome qui décrit la parabole du lancer d'épine
            if self.rect.y > 100 :
                self.remove_3()


class Epines2(pygame.sprite.Sprite):

    def __init__(self, joueur):
        super().__init__()
        self.velocity = 5
        self.joueur = joueur
        self.image = pygame.image.load('images/epine_verte.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        a, b = self.joueur.position_2_2()
        self.rect.x = a
        self.rect.y = b
        self.stck = 600
        pygame.init()
        pygame.mixer.pre_init()
        pygame.mixer.init()
        pygame.mixer.Channel(5).play(pygame.mixer.Sound('SONS/epine.wav'))

        global cptt_2
        cptt_2 = 0

    def health_bar(self,surface):
        return
    def change(self, val):
        self.rect.x=-200

    def col(self):
        global mode
        for chouette in self.joueur.game.check_collision(self, self.joueur.game.groupe_chouette.chouette):
            if chouette.rect.x > -50 and self.joueur.game.get_bouclier() == 0:
                chouette.damage(50)
                self.joueur.all_projectiles.remove(self)
        a = 500
        if self.joueur.game.get_vag5() != 0:
            a = 450
        if self.rect.y > a:
            self.joueur.all_projectiles.remove(self)

    def damage(self, amount):
        return

    def remplis(self):
        return

    def health(self):
        a = self.health
        return a

    def col2(self):
        return

    def move_bas(self):
        return

    def avancer2(self, ar):
        return

    def remove(self):
        return

    def remove_3(self):
        self.joueur.all_projectiles.remove()

    def remove_2(self):
        return

    def avancer(self):
        return

    def dessin(self, ver, background):
        global cptt_2
        if cptt_2 == 0:
            a, b = self.joueur.position_2_2()
            # print(a,b)
            self.rect.x = a
            self.rect.y = b

            cptt_2 += 1
        self.rect.x = self.rect.x - 5
        self.stck -= 5
        self.rect.y = int(0.0056 * self.stck * self.stck - 3.9709 * self.stck + 791.005) #polynome qui décrit la parabole du lancer d'épine
        if self.rect.y > 100:
            self.remove_3()

class Epines3(pygame.sprite.Sprite):

    def __init__(self, joueur):
        super().__init__()
        self.velocity = 5
        self.joueur = joueur
        self.image = pygame.image.load('images/epine_verte.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        a, b = self.joueur.position_2_3()
        self.rect.x = a
        self.rect.y = b
        self.stck = 600
        pygame.init()
        pygame.mixer.pre_init()
        pygame.mixer.init()
        pygame.mixer.Channel(5).play(pygame.mixer.Sound('SONS/epine.wav'))

        global cptt_3
        cptt_3 = 0

    def health_bar(self,surface):
        return

    def change(self, val):
        self.rect.x=-200

    def col(self):
        global mode
        for chouette in self.joueur.game.check_collision(self, self.joueur.game.groupe_chouette.chouette):
            if chouette.rect.x > -50 and self.joueur.game.get_bouclier() == 0:
                chouette.damage(50)
                self.joueur.all_projectiles.remove(self)
        a = 500
        if self.joueur.game.get_vag5() != 0:
            a = 450
        if self.rect.y > a:
            self.joueur.all_projectiles.remove(self)

    def col2(self):
        return

    def move_bas(self):
        return

    def damage(self, amount):
        return

    def remplis(self):
        return

    def health(self):
        a = self.health
        return a

    def avancer2(self, ar):
        return

    def remove(self):
        return

    def remove_3(self):
        self.joueur.all_projectiles.remove()

    def remove_2(self):
        return

    def avancer(self):
        return

    def dessin(self, ver, background):
        global cptt_3
        if cptt_3 == 0:
            a, b = self.joueur.position_2_3()
            # print(a,b)
            self.rect.x = a
            self.rect.y = b

            cptt_3 += 1
            # print('rentré')
            # print(self.rect.x,self.rect.y)
        self.rect.x = self.rect.x - 5
        self.stck -= 5
        self.rect.y = int(0.0056 * self.stck * self.stck - 3.9709 * self.stck + 791.005) #polynome qui décrit la parabole du lancer d'épine
        if self.rect.y > 100:
            self.remove_3()

class Epines4(pygame.sprite.Sprite):

    def __init__(self, joueur):
        super().__init__()
        self.velocity = 5
        self.joueur = joueur
        self.image = pygame.image.load('images/epine_verte.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        a, b = self.joueur.position_2_4()
        self.rect.x = a
        self.rect.y = b
        self.stck = 600
        pygame.init()
        pygame.mixer.pre_init()
        pygame.mixer.init()
        pygame.mixer.Channel(5).play(pygame.mixer.Sound('SONS/epine.wav'))

        global cptt_4
        cptt_4 = 0

    def health_bar(self,surface):
        return
    def change(self, val):
        self.rect.x=-200

    def col(self):
        global mode
        for chouette in self.joueur.game.check_collision(self, self.joueur.game.groupe_chouette.chouette):
            if chouette.rect.x > -50 and self.joueur.game.get_bouclier() == 0:
                chouette.damage(50)
                self.joueur.all_projectiles.remove(self)
        a = 500
        if self.joueur.game.get_vag5() != 0:
            a = 450
        if self.rect.y > a:
            self.joueur.all_projectiles.remove(self)

    def col2(self):
        return


    def move_bas(self):
        return

    def avancer2(self, ar):
        return

    def remove(self):
        return

    def remove_3(self):
        self.joueur.all_projectiles.remove()

    def remove_2(self):
        return

    def damage(self, amount):
        return

    def remplis(self):
        return

    def health(self):
        a = self.health
        return a

    def avancer(self):
        return

    def dessin(self, ver, background):
        global cptt_4
        if cptt_4 == 0:
            a, b = self.joueur.position_2_4()
            # print(a,b)
            self.rect.x = a
            self.rect.y = b

            cptt_4 += 1
            # print('rentré')
            # print(self.rect.x,self.rect.y)
        self.rect.x = self.rect.x - 5
        self.stck -= 5
        # self.rect.y = int(0.0056 * self.stck * self.stck - 2.8 * self.stck + 500.005)
        # self.rect.y = int(-0.5 * self.stck * self.stck + 2.25*self.stck + 791.005 )
        self.rect.y = int(0.0056 * self.stck * self.stck - 3.9709 * self.stck + 791.005) #polynome qui décrit la parabole du lancer d'épine
        if self.rect.y > 100:
            self.remove_3()

class Epines5(pygame.sprite.Sprite):

    def __init__(self, joueur):
        super().__init__()
        self.velocity = 5
        self.joueur = joueur
        self.image = pygame.image.load('images/epine_verte.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        a, b = self.joueur.position_2_5()
        self.rect.x = a
        self.rect.y = b
        self.stck = 600
        pygame.init()
        pygame.mixer.pre_init()
        pygame.mixer.init()
        pygame.mixer.Channel(5).play(pygame.mixer.Sound('SONS/epine.wav'))

        global cptt_5
        cptt_5 = 0

    def change(self, val):
        self.rect.x=-200

    def health_bar(self,surface):
        return

    def col(self):
        global mode
        for chouette in self.joueur.game.check_collision(self, self.joueur.game.groupe_chouette.chouette):
            if chouette.rect.x > -50 and self.joueur.game.get_bouclier() == 0:
                chouette.damage(50)
                self.joueur.all_projectiles.remove(self)
        a = 500
        if self.joueur.game.get_vag5() != 0:
            a = 450
        if self.rect.y > a:
            self.joueur.all_projectiles.remove(self)

    def col2(self):
        return

    def move_bas(self):
        return

    def avancer2(self, ar):
        return

    def damage(self, amount):
        return

    def remplis(self):
        return

    def health(self):
        a = self.health
        return a

    def remove(self):
        return

    def remove_3(self):
        self.joueur.all_projectiles.remove()

    def remove_2(self):
        return

    def avancer(self):
        return

    def dessin(self, ver, background):
        global cptt_5
        if cptt_5 == 0:
            a, b = self.joueur.position_2_5()
            # print(a,b)
            self.rect.x = a
            self.rect.y = b

            cptt_5 += 1
            # print('rentré')
            # print(self.rect.x,self.rect.y)
        self.rect.x = self.rect.x - 5
        self.stck -= 5
        # self.rect.y = int(0.0056 * self.stck * self.stck - 2.8 * self.stck + 500.005)
        # self.rect.y = int(-0.5 * self.stck * self.stck + 2.25*self.stck + 791.005 )
        self.rect.y = int(0.0056 * self.stck * self.stck - 3.9709 * self.stck + 791.005) #polynome qui décrit la parabole du lancer d'épine
        if self.rect.y > 100:
            self.remove_3()


