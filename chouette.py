import pygame

class Arbre(pygame.sprite.Sprite):

    def __init__(self,joueur):
        super(Arbre, self).__init__()
        self.image = pygame.image.load("images/tree.png")
        self.image = pygame.transform.scale(self.image, (300, 300))
        self.rect = self.image.get_rect()
        self.joueur = joueur
        #self.rect.x = -300
        self.rect.x = - 130
        self.rect.y = 230

    def bougetoi(self):
        if self.rect.x<-130:
            self.rect.x+=1

    def bougetoi2(self):
        return
    def reculetoi(self):
        if self.rect.x>-300:
            self.rect.x -= 3


class Chouette(pygame.sprite.Sprite):
    def __init__(self,joueur):
        super(Chouette,self).__init__()
        self.health = 1000
        self.max_health = 1000
        self.image = pygame.image.load("images/chouette.png")
        self.image = pygame.transform.scale(self.image, (125, 125))
        self.rect = self.image.get_rect()
        self.joueur = joueur
        #self.rect.x = 55
        self.rect.x = 55
        self.rect.y = 250
        global mort
        mort = 0
    def damage(self,amount):
        global mort
        # son quand la chouette est touchée par les épines des cactus
        pygame.init()
        pygame.mixer.pre_init()
        pygame.mixer.init()
        pygame.mixer.Channel(4).play(pygame.mixer.Sound('SONS/owl.wav'))
        self.health -= amount
        if self.health <= 0:
            self.rect.x = -115
            mort=1

    def health_bar(self,surface):
        bar_color = (189, 86, 0)
        back_bar_color = (60, 63, 60)
        a = self.health/10
        b=self.max_health/10
        bar_position = [self.rect.x + 10, self.rect.y - 20, a, 5]
        back_bar_position = [self.rect.x + 9, self.rect.y - 21, b + 2, 7]
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)

    def death(self):
        global mort
        return mort

    def bougetoi(self):
        return
    def bougetoi2(self):
        if self.rect.x<55 and mort==0:
            self.rect.x = self.rect.x + 1


    def reculetoi(self):
        if self.rect.x>-115 :
            self.rect.x -= 3


