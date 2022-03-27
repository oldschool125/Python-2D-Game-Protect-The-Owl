import pygame

class Allie(pygame.sprite.Sprite):  #Il s'agit du cactus robot


    def __init__(self,joueur):
        super().__init__()
        self.health=100
        self.max_health=100
        self.attack=10
        self.joueur = joueur
        if self.joueur.game.get_ar() % 2 == 0:
            self.image=pygame.image.load("images/cactus_allie.png")
        else:
            self.image = pygame.image.load("images/cactus_allie_2.png")
        self.rect = self.image.get_rect()
        self.image= pygame.transform.scale(self.image, (450,210))
        if self.joueur.game.get_ar()%2==0:
            self.rect.x=-300
        elif self.joueur.game.get_ar()%2==1:
            self.rect.x=900
        self.rect.y=345
        self.velocity = 1
        self.bar = 0
        global kill
        kill=0

    def remove_3(self):
        return
    def change(self, val):
        return
    def avancer2(self,ar): #En fonction de ar, il va soit avancer, soit reculer
        if ar%2==1:
            self.rect.x += 7
            if self.rect.x > 1080:
                self.joueur.all_projectiles.remove(self)
        elif ar%2==0:
            self.rect.x -= 7
            if self.rect.x < -300:
                self.joueur.all_projectiles.remove(self)
    def col2(self):
        return
    def avancer(self):
        return


    def move_bas(self):
        return

    def remove_2(self):
        return
    def remove(self):
        return
    
    def dessin(self,ver, background):
        return

    def damage(self, amount):
        return

    def remplis(self):
        return

    def health(self):
        a = self.health
        return a

    def health_bar(self,surface):
        return

    def col(self):
        global kill
        if 1:
            # son quand l'utilisateur utilise l'attaque 'robot' (touche A)
            pygame.init()
            pygame.mixer.pre_init()
            pygame.mixer.init()
            song8 = pygame.mixer.Sound('SONS/robot.wav')
            song8.play()
            for cactus in self.joueur.game.check_collision(self,self.joueur.game.all_monsters) or self.joueur.game.check_collision(self, self.joueur.game.cactus2.c2) or self.joueur.game.check_collision(self,self.joueur.game.cactus3.c3)  or self.joueur.game.check_collision(self,self.joueur.game.cactus4.c4) or self.joueur.game.check_collision(self, self.joueur.game.cactus5.c5):
                if kill < 2 and cactus.get_vagg5()<1: #Il ne tue que 2 cactus
                    cactus.damage(500)
                    song8.stop()

                elif kill==0 and cactus.get_vagg5()>=1:
                    cactus.damage(500)    #Le cactus boss ne prend que 500 dégats après collisitions (il en prendrait 1000 si on n'avait pas séparé les cas à cause de la condition kill<=2)
                    song8.stop()
                    
                kill += 1

                if self.joueur.game.get_ar() % 2 == 1:  #Faire reculer les cactus si le cactus robot arrive de la gauche vers la droite
                    cactus.reculer()
                    cactus.reculer()
                    cactus.reculer()
                    cactus.reculer()
                    cactus.reculer()
                    cactus.reculer()

                if self.joueur.game.get_ar()%2==0: #Faire avacner le cactus si le cactus robot arrive de la droite vers la gauche
                    cactus.avancer2()
                    cactus.avancer2()
                    cactus.avancer2()
                    cactus.avancer2()
                    cactus.avancer2()
                    cactus.avancer2()



