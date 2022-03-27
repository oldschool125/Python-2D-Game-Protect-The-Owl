import pygame

class Bouclier(pygame.sprite.Sprite): #Il s'agit du bouclier qui entoure la chouette

    def __init__(self, joueur):
        super(Bouclier,self).__init__()
        #Initialisation
        self.health = 200
        self.max_health = 200
        self.attack = 10
        self.joueur = joueur
        self.image = pygame.image.load("images/boucliervf.png")
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (450, 210))
        self.rect.x = -100
        self.rect.y = 184
        self.velocity = 1
        self.bar = 0
        global kill
        kill = 0

    def damage(self,amount):
        # son quand l'utilisateur utilise le bouclier pour protéger la chouette (touche R)
        pygame.init()
        pygame.mixer.pre_init()
        pygame.mixer.init()
        song9 = pygame.mixer.Sound('SONS/shield1.wav')
        song9.play()
        #for bouclier in self.joueur.game.check_collision(self, self.joueur.all_projectiles):
           # self.joueur.all_projectiles.remove()
        self.health -= amount
        if self.health <=0 :
            #Faire disparaitre le bouclier
            song9.stop()
            self.joueur.all_projectiles.remove(self)
            self.joueur.game.modif_dam(0)
            self.joueur.game.modif_bouclier(0)
            self.remplis()
            #self.rect.x = -600

    def health(self):
        return

    def remplis(self):
        #Fonction pour remplir la barre de vie du bouclier
        self.health = self.max_health



    def remove_3(self):
        return

    def change(self, val):
        return

    def avancer2(self, ar):
        return

    def avancer(self):
        return

    def move_bas(self):
        return

    def remove_2(self):
        return

    def remove(self):
        return

    def dessin(self, ver, background):
        return

    def col(self):
        global kill
    def col2(self):
        return

    def health_bar(self,surface):
        #Afficher la barre de vie du bouclier et l'update
        bar_color = (47, 221, 234)
        back_bar_color = (60, 63, 60)
        bar_position = [self.rect.x + 130, self.rect.y - 20, self.health, 5]
        back_bar_position = [self.rect.x + 130, self.rect.y - 21, self.max_health, 7]
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)