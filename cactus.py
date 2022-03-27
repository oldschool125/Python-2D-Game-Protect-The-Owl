import pygame
import random
import time
import sys


class Cactus(pygame.sprite.Sprite):

    def __init__(self,joueur):
        super(Cactus, self).__init__()
        global vagg2, vagg3, vagg4, vagg5
        vagg2 = 0
        vagg3=0
        vagg4=0
        vagg5=0
        #Initialisation du cactus
        if vagg2==0 and vagg3==0 and vagg4==0 :
            self.health = 100
            self.max_health = 100
            self.attack = 10
            self.image = pygame.image.load("images/cactus.png")
        self.joueur = joueur
        self.rect = self.image.get_rect()
        self.rect.x=1100 + random.randint(0,1000)
        self.rect.y=400
        self.velocity = 1
        self.bar = 0
        self.normal = self.image
        self.angle = 0
        global compteur
        global kill
        #Différents compteurs pour compter le nombre de kills ou au autres
        kill=0
        global kill2
        kill2=0
        global killtest
        killtest=0
        compteur = 0
        ver=False
        fait=0
        global cpt3
        cpt3=0
        global cppt
        cppt=0
        global X
        global Y
        X= self.rect.x 
        Y=self.rect.y
        global fin
        fin =0
        global c
        c=0

    def fin(self):
        #Fonction qui retourne si le boss est mort (donc fin du jeu) ou non
        global fin
        return fin

    def get_vagg5(self):
        global vagg5
        return vagg5
    def get_kill2(self):
        global kill2#, killtest
        #if kill2>killtest:
        #    print(kill2)
        #    killtest=kill2
        return kill2

    def avancer2(self):
        global c
        if self.rect.x > c:
            self.rect.x -= 1.5 * self.velocity

    #def traj(self,x):
    #    return (0.0056 * x ** 2 - 3.9709 * x + 791.005)

    #def dessin(self, ver,background):
        # dessiner les rectangles
        #pygame.draw.rect(background, (255, 0, 0), (95, 460, 10, 40), 0)
        #pygame.draw.rect(background, (0, 0, 0), (600, 500, 50, 10), 0)

    #    x = 100
    #    y = 450
    #    rayon = 10

        # dessiner les cercles
    #    pygame.draw.circle(background, (255, 255, 255), (x, y), rayon, 0)

        # mettre à jour l'affichage
    #    pygame.display.flip()

    #    pygame.time.delay(1500)

    #    if ver :
    #        x = x - 5  # x devient x plus cinq,
    #        # on avance vers la gauche
    #        y = int(traj(x))  # y en fonction de x
    #        # le int pour avoir un entier
    #        # (pour les coordonnées)

    def meta(self,vague2,vague3,vague4,vague5):
        #Changement du cactus en fonction de la vague
        global vagg2, vagg3, vagg4, vagg5
        if vague2>=1 :
            if vagg2==0:
                self.image = pygame.image.load("images/cactus_v2.png")
                self.health = 200
                self.max_health = 200
                self.attack = 20
        if vague3>=1 :
            if vagg3==0:
                self.image=pygame.image.load("images/cactus_v3.png")
                self.health = 300
                self.max_health = 300
                self.attack = 30
        if vague4>=1:
            if vagg4 == 0:
                self.image=pygame.image.load("images/cactus_v4.png")
                self.health = 500
                self.max_health = 500
                self.attack = 50
        if vague5>=1:
            if vagg5==0:
                self.image = pygame.image.load("images/bossboss2.png")
                self.image = pygame.transform.scale(self.image, (966, 450))
                self.normal = self.image
                self.health = 10000
                self.max_health = 10000
                self.attack = 200
                self.rect.y = 360
                self.rect.x = 1000
            vagg5 += 1

    def tourne(self,sens):
        #Fonction pour faire tourner le Boss final
        if vagg5>=1:
            if sens==1:
                self.angle -= 0.5
            else:
                self.angle += 0.5
            self.image = pygame.transform.rotozoom(self.normal, self.angle, 0.5)
            self.rect = self.image.get_rect(center = self.rect.center)
    def compteur(self):
        global compteur
        return compteur
    def modif_compteur(self,new):
        global compteur
        compteur = new

    def get_kill(self):
        #Donne le nombre de kills
        global kill
        return kill
    def modif_kill(self,new):
        global kill
        #Modifier le nombre de kills pour le réinitiatiliser suite à une nouvelle vague
        kill=new
    def zero(self,ver):
        global bar_position, fait
        fait=0
        if ver==True:
            compteur=0
            bar_position[2] = 0
            feu=0
            ver=False
            fait=1



    def reposition(self):
        #Repositionne le cactus suite à une nouvelle vague
        global vagg5
        self.rect.x = 1600 + random.randint(0,1000)
        if vagg5==1:
            self.rect.x = 3500
        self.health = self.max_health

    def damage(self,amount):
        #Fonction pour que le cactus prenne des dégats
        global compteur, kill, kill2, vagg5,fin
        self.health -= amount
        # son quand le cactus est blessé/touché et perd de la vie
        pygame.mixer.Channel(4).play(pygame.mixer.Sound('SONS/crack.wav'))
        pygame.mixer.Channel(5).play(pygame.mixer.Sound('SONS/crack.wav'))
        pygame.mixer.Channel(6).play(pygame.mixer.Sound('SONS/crack.wav'))
        if self.health <= 0 :
            kill+=1
            kill2+=1
            # son quand un cactus meurt
            pygame.mixer.Channel(7).play(pygame.mixer.Sound('SONS/end.wav'))
            if compteur <= 950:
                compteur += 50
            self.rect.x = 1100 + random.randint(0,1000)
            if vagg5>=1:
                fin=1
            self.health = self.max_health

    def special_bar(self, surface):
        #Faire apparaitre la barre spéciale et la mettre à jour avec le compteur (attaque ultime)
        global feu, bar_position, fait, compteur
        feu=0
        fait=0
        if compteur>= 1000:
            feu = 1
        bar_color = (237,112,9)
        back_bar_color = (60,63,60)
        bar_position = [40, 700, compteur, 7]
        back_bar_position = [40, 699, 1000, 10]
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface,bar_color, bar_position)
        

    def bomb_bar(self, surface, barre):
        #Faire apparaitre la barre de la bombe et la mettre à jour avec le compteur barre
        bar_color = (237, 0, 0)
        back_bar_color = (60, 63, 60)
        bar_position = [800, 100, barre, 7]
        back_bar_position = [800, 99, 100, 10]
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)

    def canon_bar(self, surface, barre2):
        # Faire apparaitre la barre du canon et la mettre à jour avec le compteur barre2
        bar_color = (237, 237, 30)
        back_bar_color = (60, 63, 60)
        bar_position = [650, 100, barre2, 7]
        back_bar_position = [650, 99, 100, 10]
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)

    def bouclier_bar(self,surface,barre3): #pareil
        bar_color = (47, 221, 234)
        back_bar_color = (60, 63, 60)
        bar_position = [950, 100, barre3, 7]
        back_bar_position = [950, 99, 100, 10]
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)


    def allie_bar(self, surface, barre3):
        bar_color = (200, 200, 200)
        back_bar_color = (60, 63, 60)
        bar_position = [500, 100, barre3, 7]
        back_bar_position = [500, 99, 100, 10]
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)

    def update_health_bar(self, surface):
        # Faire apparaitre la barre de vie du cactus et la mettre à jour avec self.health
        global vagg2, vagg3, vagg4
        bar_color = (0,185,0)
        back_bar_color = (60,63,60)
        if vagg2>=1:
            a=self.health/2
            b=self.max_health/2
            bar_color = (237, 168, 9)
        if vagg3>=1:
            a=self.health/3
            b=self.max_health/3
            bar_color = (237,50,9)
        if vagg4>=1:
            a=self.health/5
            b=self.max_health/5
            bar_color = (82,0,0)
        if vagg5>=1:
            bar_position = [ 40, 700-20, self.health/10, 5]
            back_bar_position = [40, 700 - 21, self.max_health/10 + 2, 7]
            bar_color = (255,55,161)
        if vagg2==0 and vagg3==0 and vagg4==0 and vagg5==0:
            a=self.health
            b=self.max_health
        if vagg5<1:
            bar_position = [self.rect.x + 10, self.rect.y - 20, a, 5]
            back_bar_position = [self.rect.x + 9, self.rect.y - 21, b + 2, 7]

        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface,bar_color, bar_position)


    def check_kills(self):
        global feu
        return feu

    def reculer(self):
        if self.rect.x<1080:
            #faire reculer le cactus une fois qu'il est arrivé à gauche de l'écran
            self.rect.x += 1.5*self.velocity

    def avancer(self,ver):
        global cpt3, c
        #print(self.position_2())
        self.modif_position()
        self.tourne(cpt3)
        #Faire avancer le cactus et le faire reculer en fonction de sa position sur l'écran
        a=300
        b=1000
        c=0
        if vagg5!=0:
            a=100
            b=850
        if self.rect.x <= c:
            cpt3 = 1
        if self.rect.x>= b :
            cpt3=0
        if self.rect.x==a and ver==1:
            cpt3 = 1
        if ver==0 :
            if self.rect.x > c and cpt3==0:
                self.rect.x -= 0.5 *self.velocity
            if cpt3==1:
                if self.rect.x>=c:
                    self.reculer()
        elif ver==1 :
            if self.rect.x > a and cpt3==0:
                self.rect.x -= 0.5 * self.velocity
            if self.rect.x < a:
                self.reculer()
            if cpt3 == 1:
                if self.rect.x >= a :
                    self.reculer()
            if self.rect.x == b:
                cpt3 = 0


    def sauter(self):
        #Faire sauter le cactus
        global cppt, vagg5
        if cppt > 200 and cppt < 1700 and vagg5==0:
            if self.rect.y <= 355 and cppt % 2 == 1:
                self.rect.y += 50 * self.velocity

            elif self.rect.y >= 255 and cppt % 2 == 0:
                self.rect.y -= 1 * self.velocity
            if cppt == 1699:
                cppt = 0
                self.rect.y = 400
        cppt+=1
    def modif_position(self):
        global X,Y
        X = self.rect.x
        Y= self.rect.y
    def position_2(self):
        global X,Y
        #print(self.rect.x,self.rect.y)
        return X,Y
    def test(self):
        a,b = self.position_2()
        #print(a,b)


class Cactus2(pygame.sprite.Sprite):

    def __init__(self, joueur):
        super().__init__()
        if vagg2 == 0 and vagg3 == 0 and vagg4 == 0:
            self.health = 100
            self.max_health = 100
            self.attack = 10
            self.image = pygame.image.load("images/cactus.png")
        self.joueur = joueur
        self.rect = self.image.get_rect()
        self.rect.x = 1100 + random.randint(0, 1000)
        self.rect.y = 400
        self.velocity = 1
        self.bar = 0
        self.com = 0
        ver=False
        fait=0
        global cpt3_2
        cpt3_2 = 0
        global cppt_2
        cppt_2 = 0
        global X2,Y2

    def reposition(self):
        self.rect.x = 1600 + random.randint(0, 1000)
        self.health = self.max_health

    def get_vagg5(self):
        global vagg5
        return vagg5
    def avancer2(self):
        if self.rect.x > 0:
            self.rect.x -= 1.5 * self.velocity

    def meta(self, vague2, vague3, vague4):
        global vagg2, vagg3, vagg4
        if vague2 >= 1:
            if vagg2 == 0:
                self.image = pygame.image.load("images/cactus_v2.png")
                self.health = 200
                self.max_health = 200
                self.attack = 20
        if vague3 >= 1:
            if vagg3 == 0:
                self.image = pygame.image.load("images/cactus_v3.png")
                self.health = 300
                self.max_health = 300
                self.attack = 30
        if vague4 >= 1:
            if vagg4 == 0:
                self.image = pygame.image.load("images/cactus_v4.png")
                self.health = 500
                self.max_health = 500
                self.attack = 50


            # vagg4+=1 #cactus 5
            # vagg2=0
            # vagg3 += 1 #cactus 5 avec vagg2+=1

    def zero(self, ver):
        global compteur
        global bar_position, fait
        fait = 0
        if ver == True:
            compteur = 0
            bar_position[2] = 0
            feu = 0
            ver = False
            fait = 1

    def update_health_bar(self, surface):
        global vagg2, vagg3, vagg4, vagg5
        if vagg5>0:
            self.rect.x=1150
        bar_color = (0, 185, 0)
        back_bar_color = (60, 63, 60)
        if vagg2 >= 1:
            a = self.health / 2
            b = self.max_health / 2
            bar_color = (237, 168, 9)
        if vagg3 >= 1:
            a = self.health / 3
            b = self.max_health / 3
            bar_color = (237, 50, 9)
        if vagg4 >= 1:
            a = self.health / 5
            b = self.max_health / 5
            bar_color = (82, 0, 0)
        if vagg2 == 0 and vagg3 == 0 and vagg4 == 0:
            a = self.health
            b = self.max_health
        bar_position = [self.rect.x + 10, self.rect.y - 20, a, 5]
        back_bar_position = [self.rect.x + 9, self.rect.y - 21, b + 2, 7]
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)

    def damage(self, amount):
        global compteur, kill, kill2
        self.health -= amount
        pygame.mixer.Channel(4).play(pygame.mixer.Sound('SONS/crack.wav'))
        pygame.mixer.Channel(5).play(pygame.mixer.Sound('SONS/crack.wav'))
        pygame.mixer.Channel(6).play(pygame.mixer.Sound('SONS/crack.wav'))
        if self.health <= 0:
            kill+=1
            kill2+=1
            pygame.mixer.Channel(7).play(pygame.mixer.Sound('SONS/end.wav'))
            if compteur <= 950:
                compteur += 50
            self.rect.x = 1100 + random.randint(0, 600)
            self.health = self.max_health


    def reculer(self):
        if self.rect.x < 1080:
            self.rect.x += 1.5 * self.velocity

    def avancer(self, ver):
        global cpt3_2
        self.modif_position()
        if self.rect.x <= 0:
            cpt3_2 = 1
        if self.rect.x >= 1000:
            cpt3_2 = 0
        if self.rect.x == 300 and ver == 1:
            cpt3_2 = 1
        if ver == 0:
            if self.rect.x > 0 and cpt3_2 == 0:
                self.rect.x -= 0.5 * self.velocity
            if cpt3_2 == 1:
                if self.rect.x >= 0:
                    self.reculer()
        elif ver == 1:
            if self.rect.x > 300 and cpt3_2 == 0:
                self.rect.x -= 0.5 * self.velocity
            if self.rect.x < 300:
                self.reculer()
            if cpt3_2 == 1:
                if self.rect.x >= 300:
                    self.reculer()
            if self.rect.x == 1000:
                cpt3_2 = 0

    def sauter(self):
        global cppt_2
        if cppt_2 > 1555 and cppt_2 < 3500:
            if self.rect.y <= 355 and cppt_2 % 2 == 1:
                self.rect.y += 50 * self.velocity

            elif self.rect.y >= 255 and cppt_2 % 2 == 0:
                self.rect.y -= 1 * self.velocity
            if cppt_2 == 3499:
                cppt_2 = 0
                self.rect.y = 400
        cppt_2 += 1
    def modif_position(self):
        global X2,Y2
        X2 = self.rect.x
        Y2= self.rect.y
    def position_2(self):
        global X2,Y2
        #print(self.rect.x,self.rect.y)
        return X2,Y2
    def test(self):
        a,b = self.position_2()
        #print(a,b)



class Cactus3(pygame.sprite.Sprite):

    def __init__(self, joueur):
        super().__init__()
        if vagg2 == 0 and vagg3 == 0 and vagg4 == 0:
            self.health = 100
            self.max_health = 100
            self.attack = 10
            self.image = pygame.image.load("images/cactus.png")
        self.joueur = joueur
        self.rect = self.image.get_rect()
        self.rect.x = 1100 + random.randint(0, 1000)
        self.rect.y = 400
        self.velocity = 1
        self.bar = 0
        self.com = 0
        ver=False
        fait=0
        global cpt3_3
        cpt3_3 = 0
        global cppt_3
        cppt_3 = 0
        global X3,Y3

    def meta(self, vague2, vague3, vague4):
        global vagg2, vagg3, vagg4
        if vague2 >= 1:
            if vagg2 == 0:
                self.image = pygame.image.load("images/cactus_v2.png")
                self.health = 200
                self.max_health = 200
                self.attack = 20
        if vague3 >= 1:
            if vagg3 == 0:
                self.image = pygame.image.load("images/cactus_v3.png")
                self.health = 300
                self.max_health = 300
                self.attack = 30
        if vague4 >= 1:
            if vagg4 == 0:
                self.image = pygame.image.load("images/cactus_v4.png")
                self.health = 500
                self.max_health = 500
                self.attack = 50
            # vagg4+=1 #cactus 5
            # vagg2=0
            # vagg3 += 1 #cactus 5 avec vagg2+=1

    def get_vagg5(self):
        global vagg5
        return vagg5

    def reposition(self):
        self.rect.x = 1600 + random.randint(0, 1000)
        self.health = self.max_health
    def avancer2(self):
        if self.rect.x > 0:
            self.rect.x -= 1.5 * self.velocity

    def zero(self, ver):
        global bar_position, fait
        fait = 0
        if ver == True:
            self.compteur = 0
            bar_position[2] = 0
            feu = 0
            ver = False
            fait = 1

    def damage(self, amount):
        global compteur, kill, kill2
        self.health -= amount
        pygame.mixer.Channel(4).play(pygame.mixer.Sound('SONS/crack.wav'))
        pygame.mixer.Channel(5).play(pygame.mixer.Sound('SONS/crack.wav'))
        pygame.mixer.Channel(6).play(pygame.mixer.Sound('SONS/crack.wav'))
        if self.health <= 0:
            kill+=1
            kill2+=1
            pygame.mixer.Channel(7).play(pygame.mixer.Sound('SONS/end.wav'))
            if compteur <= 950:
                compteur += 50
            self.rect.x = 1100 + random.randint(0, 600)
            self.health = self.max_health

    def update_health_bar(self, surface):
        global vagg2, vagg3, vagg4, vagg5
        if vagg5>0:
            self.rect.x=1150
        bar_color = (0, 185, 0)
        back_bar_color = (60, 63, 60)
        if vagg2 >= 1:
            a = self.health / 2
            b = self.max_health / 2
            bar_color = (237, 168, 9)
        if vagg3 >= 1:
            a = self.health / 3
            b = self.max_health / 3
            bar_color = (237, 50, 9)
        if vagg4 >= 1:
            a = self.health / 5
            b = self.max_health / 5
            bar_color = (82, 0, 0)
        if vagg2 == 0 and vagg3 == 0 and vagg4 == 0:
            a = self.health
            b = self.max_health
        bar_position = [self.rect.x + 10, self.rect.y - 20, a, 5]
        back_bar_position = [self.rect.x + 9, self.rect.y - 21, b + 2, 7]
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)

    def check_kills(self):
        global feu
        return feu

    def reculer(self):
        if self.rect.x < 1080:
            self.rect.x += 1.5 * self.velocity

    def avancer(self, ver):
        global cpt3_3
        self.modif_position()
        if self.rect.x <= 0:
            cpt3_3 = 1
        if self.rect.x >= 1000:
            cpt3_3 = 0
        if self.rect.x == 300 and ver == 1:
            cpt3_3 = 1
        if ver == 0:
            if self.rect.x > 0 and cpt3_3 == 0:
                self.rect.x -= 0.5 * self.velocity
            if cpt3_3 == 1:
                if self.rect.x >= 0:
                    self.reculer()
        elif ver == 1:
            if self.rect.x > 300 and cpt3_3 == 0:
                self.rect.x -= 0.5 * self.velocity
            if self.rect.x < 300:
                self.reculer()
            if cpt3_3 == 1:
                if self.rect.x >= 300:
                    self.reculer()
            if self.rect.x == 1000:
                cpt3_3 = 0

    def sauter(self):
        global cppt_3
        if cppt_3>564 and cppt_3<2500:
            if self.rect.y <= 355 and cppt_3 % 2 == 1:
                self.rect.y += 50 * self.velocity


            elif self.rect.y >= 255 and cppt_3 % 2 == 0:
                self.rect.y -= 1 * self.velocity


            if cppt_3==2499:
                cppt_3=0
                self.rect.y=400
        cppt_3 += 1
    def modif_position(self):
        global X3,Y3
        X3 = self.rect.x
        Y3= self.rect.y
    def position_2(self):
        global X3,Y3
        #print(self.rect.x,self.rect.y)
        return X3,Y3
    def test(self):
        a,b = self.position_2()
        #print(a,b)


class Cactus4(pygame.sprite.Sprite):

    def __init__(self, joueur):
        super().__init__()
        if vagg2 == 0 and vagg3 == 0 and vagg4 == 0:
            self.health = 100
            self.max_health = 100
            self.attack = 10
            self.image = pygame.image.load("images/cactus.png")
        self.joueur = joueur
        self.rect = self.image.get_rect()
        self.rect.x = 1100 + random.randint(0, 1000)
        self.rect.y = 400
        self.velocity = 1
        self.bar = 0
        self.com = 0
        ver = False
        fait = 0
        global cpt3_4
        cpt3_4 = 0
        global cppt_4
        cppt_4 = 0
        global X4,Y4

    def meta(self, vague2, vague3, vague4):
        global vagg2, vagg3, vagg4
        if vague2 >= 1:
            if vagg2 == 0:
                self.image = pygame.image.load("images/cactus_v2.png")
                self.health = 200
                self.max_health = 200
                self.attack = 20
        if vague3 >= 1:
            if vagg3 == 0:
                self.image = pygame.image.load("images/cactus_v3.png")
                self.health = 300
                self.max_health = 300
                self.attack = 30
        if vague4 >= 1:
            if vagg4 == 0:
                self.image = pygame.image.load("images/cactus_v4.png")
                self.health = 500
                self.max_health = 500
                self.attack = 50
            # vagg4+=1 #cactus 5
            # vagg2=0
            # vagg3 += 1 #cactus 5 avec vagg2+=1
    def get_vagg5(self):
        global vagg5
        return vagg5

    def reposition(self):
        self.rect.x = 1600 + random.randint(0, 1000)
        self.health = self.max_health

    def zero(self, ver):
        global bar_position, fait
        fait = 0
        if ver == True:
            self.compteur = 0
            bar_position[2] = 0
            feu = 0
            ver = False
            fait = 1

    def damage(self, amount):
        global compteur, kill, kill2
        self.health -= amount
        pygame.mixer.Channel(4).play(pygame.mixer.Sound('SONS/crack.wav'))
        pygame.mixer.Channel(5).play(pygame.mixer.Sound('SONS/crack.wav'))
        pygame.mixer.Channel(6).play(pygame.mixer.Sound('SONS/crack.wav'))
        if self.health <= 0:
            kill+=1
            kill2+=1
            pygame.mixer.Channel(7).play(pygame.mixer.Sound('SONS/end.wav'))
            if compteur <= 950:
                compteur += 50
            self.rect.x = 1100 + random.randint(0, 1000)
            self.health = self.max_health

    def update_health_bar(self, surface):
        global vagg2, vagg3, vagg4, vagg5
        if vagg5>0:
            self.rect.x=1150
        bar_color = (0, 185, 0)
        back_bar_color = (60, 63, 60)
        if vagg2 >= 1:
            a = self.health / 2
            b = self.max_health / 2
            bar_color = (237, 168, 9)
        if vagg3 >= 1:
            a = self.health / 3
            b = self.max_health / 3
            bar_color = (237, 50, 9)
        if vagg4 >= 1:
            a = self.health / 5
            b = self.max_health / 5
            bar_color = (82, 0, 0)
        if vagg2 == 0 and vagg3 == 0 and vagg4 == 0:
            a = self.health
            b = self.max_health
        bar_position = [self.rect.x + 10, self.rect.y - 20, a, 5]
        back_bar_position = [self.rect.x + 9, self.rect.y - 21, b + 2, 7]
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)


    def reculer(self):
        if self.rect.x < 1080:
            self.rect.x += 1.5 * self.velocity

    def avancer2(self):
        if self.rect.x > 0:
            self.rect.x -= 1.5 * self.velocity

    def avancer(self, ver):
        global cpt3_4
        self.modif_position()
        if self.rect.x <= 0:
            cpt3_4 = 1
        if self.rect.x >= 1000:
            cpt3_4 = 0
        if self.rect.x == 300 and ver == 1:
            cpt3_4 = 1
        if ver == 0:
            if self.rect.x > 0 and cpt3_4 == 0:
                self.rect.x -= 0.5 * self.velocity
            if cpt3_4 == 1:
                if self.rect.x >= 0:
                    self.reculer()
        elif ver == 1:
            if self.rect.x > 300 and cpt3_4 == 0:
                self.rect.x -= 0.5 * self.velocity
            if self.rect.x < 300:
                self.reculer()
            if cpt3_4 == 1:
                if self.rect.x >= 300:
                    self.reculer()
            if self.rect.x == 1000:
                cpt3_4 = 0

    def sauter(self):
        global cppt_4
        if cppt_4 > 1672 and cppt_4 < 3200:
            if self.rect.y <= 355 and cppt_4 % 2 == 1:
                self.rect.y += 50 * self.velocity

            elif self.rect.y >= 255 and cppt_4 % 2 == 0:
                self.rect.y -= 1 * self.velocity
            if cppt_4 == 3199:
                cppt_4 = 0
                self.rect.y = 400
        cppt_4 += 1
    def modif_position(self):
        global X4,Y4
        X4 = self.rect.x
        Y4= self.rect.y
    def position_2(self):
        global X4,Y4
        #print(self.rect.x,self.rect.y)
        return X4,Y4
    def test(self):
        a,b = self.position_2()
        #print(a,b)


class Cactus5(pygame.sprite.Sprite):

    def __init__(self, joueur):
        super().__init__()
        if vagg2 == 0 and vagg3 == 0 and vagg4 == 0:
            self.health = 100
            self.max_health = 100
            self.attack = 10
            self.image = pygame.image.load("images/cactus.png")
        self.joueur = joueur
        self.rect = self.image.get_rect()
        self.rect.x = 1100 + random.randint(0, 1000)
        self.rect.y = 400
        self.velocity = 1
        self.bar = 0
        self.com = 0
        ver = False
        fait = 0
        global cpt3_5
        cpt3_5 = 0
        global cppt_5
        cppt_5 = 0
        global X5,Y5

    def meta(self, vague2, vague3, vague4):
        global vagg2, vagg3, vagg4
        if vague2 >= 1:
            if vagg2 == 0:
                self.image = pygame.image.load("images/cactus_v2.png")
                self.health = 200
                self.max_health = 200
                self.attack = 20
            vagg2 += 1
        if vague3 >= 1:
            if vagg3 == 0:
                self.image = pygame.image.load("images/cactus_v3.png")
                self.health = 300
                self.max_health = 300
                self.attack = 30
            vagg3 += 1
            vagg2=0
        if vague4 >= 1:
            if vagg4 == 0:
                self.image = pygame.image.load("images/cactus_v4.png")
                self.health = 500
                self.max_health = 500
                self.attack = 50
            vagg4+=1 #cactus 5
            vagg3=0
         #cactus 5 avec vagg2+=1

    def reposition(self):

        self.rect.x = 1600 + random.randint(0, 1000)
        self.health = self.max_health
    def avancer2(self):
        if self.rect.x > 0:
            self.rect.x -= 1.5 * self.velocity
    def get_vagg5(self):
        global vagg5
        return vagg5

    def zero(self, ver):
        global bar_position, fait
        fait = 0
        if ver == True:
            self.compteur = 0
            bar_position[2] = 0
            feu = 0
            ver = False
            fait = 1

    def damage(self, amount):
        global compteur, kill, kill2
        self.health -= amount
        pygame.mixer.Channel(4).play(pygame.mixer.Sound('SONS/crack.wav'))
        pygame.mixer.Channel(5).play(pygame.mixer.Sound('SONS/crack.wav'))
        pygame.mixer.Channel(6).play(pygame.mixer.Sound('SONS/crack.wav'))
        if self.health <= 0:
            kill+=1
            kill2+=1
            pygame.mixer.Channel(7).play(pygame.mixer.Sound('SONS/end.wav'))
            if compteur <= 950:
                compteur += 50
            self.rect.x = 1100 + random.randint(0, 600)
            self.health = self.max_health

    def update_health_bar(self, surface):
        global vagg2, vagg3, vagg4, vagg5
        if vagg5>0:
            self.rect.x=1150
        bar_color = (0, 185, 0)
        back_bar_color = (60, 63, 60)
        if vagg2 >= 1:
            a = self.health / 2
            b = self.max_health / 2
            bar_color = (237, 168, 9)
        if vagg3 >= 1:
            a = self.health / 3
            b = self.max_health / 3
            bar_color = (237, 50, 9)
        if vagg4 >= 1:
            a = self.health / 5
            b = self.max_health / 5
            bar_color = (82, 0, 0)
        if vagg2 == 0 and vagg3 == 0 and vagg4 == 0:
            a = self.health
            b = self.max_health
        bar_position = [self.rect.x + 10, self.rect.y - 20, a, 5]
        back_bar_position = [self.rect.x + 9, self.rect.y - 21, b + 2, 7]
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)


    def reculer(self):
        if self.rect.x < 1080:
            self.rect.x += 1.5 * self.velocity

    def avancer(self, ver):
        global cpt3_5
        self.modif_position()
        if self.rect.x <= 0:
            cpt3_5 = 1
        if self.rect.x >= 1000:
            cpt3_5 = 0
        if self.rect.x == 300 and ver == 1:
            cpt3_5 = 1
        if ver == 0:
            if self.rect.x > 0 and cpt3_5 == 0:
                self.rect.x -= 0.5 * self.velocity
            if cpt3_5 == 1:
                if self.rect.x >= 0:
                    self.reculer()
        elif ver == 1:
            if self.rect.x > 300 and cpt3_5 == 0:
                self.rect.x -= 0.5 * self.velocity
            if self.rect.x < 300:
                self.reculer()
            if cpt3_5 == 1:
                if self.rect.x >= 300:
                    self.reculer()
            if self.rect.x == 1000:
                cpt3_5 = 0

    def sauter(self):
        global cppt_5
        if cppt_5 > 1231 and cppt_5 < 4200:
            if self.rect.y <= 355 and cppt_5 % 2 == 1:
                self.rect.y += 50 * self.velocity

            elif self.rect.y >= 255 and cppt_5 % 2 == 0:
                self.rect.y -= 1 * self.velocity
            if cppt_5 == 4199:
                cppt_5 = 0
                self.rect.y = 400
        cppt_5 += 1
    def modif_position(self):
        global X5,Y5
        X5 = self.rect.x
        Y5= self.rect.y
    def position_2(self):
        global X5,Y5
        #print(self.rect.x,self.rect.y)
        return X5,Y5
    def test(self):
        a,b = self.position_2()
        #print(a,b)




