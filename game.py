import pygame
from joueur import Player
from cactus import *
from cactus2 import *
from cactus3 import *
from cactus4 import *
from cactus5 import *
from chouette import *
from groupe_chouette import *
from groupe_bouclier import *
from cactus_allie import Allie
import time
from joueur import *
import random
from menu import *
from meteorite import Meteorite as meteorite
from meteorite import Bomb as bomb
import os
from epines import Epines as epines
 
class Game():
    def __init__(self,cactus):
        pygame.init()
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        pygame.display.set_caption("Protect The Owl")
        self.cactus=cactus
        self.DISPLAY_W, self.DISPLAY_H = 1080, 720
        self.display = pygame.Surface((self.DISPLAY_W,self.DISPLAY_H))
        self.window = pygame.display.set_mode(((self.DISPLAY_W,self.DISPLAY_H)))
        self.font_name = 'freak.TTF'
        self.BLACK, self.WHITE ,self.BROWN= (0, 0, 0), (255, 255, 255),(97,44,0)
        self.main_menu = MainMenu(self)
        self.story0 = Story0Menu(self)
        self.story1 = Story1Menu(self)
        self.controls = ControlsMenu(self)
        self.credits = CreditsMenu(self)
        self.quit = QuitMenu(self)
        self.curr_menu = self.main_menu
        self.player = Player(self)
        self.cactus2=groupe_2(self)
        self.cactus3=groupe_3(self)
        self.cactus4=groupe_4(self)
        self.cactus5=groupe_5(self)
        self.groupe_arbre = groupe_arbre(self)
        self.groupe_chouette = groupe_chouette(self)
        self.groupe_bouclier = groupe_bouclier(self)
        self.all_monsters = pygame.sprite.Group()
        self.pressed={}
        self.spawn_cactus()
        self.cactus2.launch_c2()
        self.cactus3.launch_c3()
        self.cactus4.launch_c4()
        self.cactus5.launch_c5()
        self.groupe_arbre.launch_arbre()
        self.groupe_chouette.launch_chouette()
        #self.spawn_cactus2()
        #self.spawn_cactus3()
        #self.spawn_cactus4()
        #self.spawn_cactus5()


    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)


    def spawn_cactus(self):
        cactus= Cactus(self)
        self.all_monsters.add(cactus)
    def spawn_cactus2(self):
        cactus2=Cactus2(self)
        self.all_monsters2.add(cactus2)
    def spawn_cactus3(self):
        cactus3=Cactus3(self)
        self.all_monsters.add(cactus3)
    def spawn_cactus4(self):
        cactus4=Cactus4(self)
        self.all_monsters.add(cactus4)
    def spawn_cactus5(self):
        cactus5=Cactus5(self)
        self.all_monsters.add(cactus5)
 
    def game_loop(self):
        pygame.init()
        pygame.mixer.pre_init()
        pygame.mixer.init()
        song = pygame.mixer.Sound('SONS/potc.wav')
        # son du vent en background
        song2 = pygame.mixer.Sound('SONS/windv.wav')
        song10 = pygame.mixer.Sound('SONS/cod.wav')
        # dimensions de la fenetre (largeur, longueur) --> renvoie une surface;  pour l'utiliser
        screen = pygame.display.set_mode((1080, 720))
        # importer le chargement de l'arrière plan du jeu
        background = pygame.image.load("images/le_desert.jpg")
        background = pygame.transform.scale(background, (2741, 720))
        pausebutton = pygame.image.load("images/pause.png")
        pausebutton = pygame.transform.scale(pausebutton, (100,100))
        icone_bomb = pygame.image.load("images/icone_bomb.png")
        icone_bomb = pygame.transform.scale(icone_bomb,(100,100))
        icone_bouclier = pygame.image.load("images/icone_bouclier.png")
        icone_bouclier = pygame.transform.scale(icone_bouclier,(100,100))
        pausemenu = pygame.image.load('images/pausemenu.png')
        pausemenu = pygame.transform.scale(pausemenu, (1080,720))
        r1 = pygame.image.load('images/r1.png')
        r1 = pygame.transform.scale(r1,(200,200))
        r11 = pygame.transform.scale(r1,(40,40))
        r2 = pygame.image.load('images/r2.png')
        r2 = pygame.transform.scale(r2,(200,200))
        r22 = pygame.transform.scale(r2,(40,40))
        r3 = pygame.image.load('images/r3.png')
        r3 = pygame.transform.scale(r3,(200,200))
        r33 = pygame.transform.scale(r3,(40,40))
        r4 = pygame.image.load('images/r4.png')
        r4 = pygame.transform.scale(r4,(200,200))
        r44 = pygame.transform.scale(r4,(40,40))
        r5 = pygame.image.load('images/r5.png')
        r5 = pygame.transform.scale(r5,(200,200))
        r55 = pygame.transform.scale(r5,(40,40))
        gameover = pygame.image.load("images/gameover.png")
        gameover = pygame.transform.scale(gameover,(1080,720))
        win = pygame.image.load("images/win.png")
        win = pygame.transform.scale(win, (1080,720))
        music = pygame.image.load("images/music.png")
        music = pygame.transform.scale(music,(25,25))
        n = pygame.image.load("images/m.png")
        n = pygame.transform.scale(n,(12,12))
        pause1 = pygame.image.load("images/pause.png")
        pause1 = pygame.transform.scale(pause1,(25,25))
        p = pygame.image.load("images/p.png")
        p = pygame.transform.scale(p,(12,12))
        a = pygame.image.load("images/a.png")
        a = pygame.transform.scale(a,(20,20))
        icone_pomp = pygame.image.load("images/icone_pomp.png")
        icone_pomp = pygame.transform.scale(icone_pomp,(100,100))
        icone_cactus = pygame.image.load("images/icone_cactus.png")
        icone_cactus = pygame.transform.scale(icone_cactus, (100, 100))
        # charger notre jeu
        game = Game(self.cactus)
        # c'est l'axe des abscisses
        x = 0
        cpt=10
        cpt2=1
        # maintient la fenetre ouverte
        temps=0
        temps2=0
        temps3=0
        barre=0
        barre2=0
        barre3=0
        barre4=0
        tps=0
        pause = False
        play=0
        pygame.init()
        pygame.mixer.pre_init()
        pygame.mixer.init()
        song = pygame.mixer.Sound('SONS/potc.wav')
        ver2=1
        ver=0
        cptv=0
        cpt3=0
        vag2=0
        global ar
        ar=0
        vag3=0
        vag4=0
        global vag5
        vag5=0
        tE = 0
        tE2=0
        tE3=0
        tE4=0
        tE5=0
        ral = 0
        ral2=0
        cc=1
        arret = 0
        ar2=0
        #ts1,ts2,ts3,ts4,ts5=0,0,0,0,0

        congrats = 0
        gover = 0
        round1 = 0
        round2 = 0
        round3 = 0
        round4 = 0
        fround = 0

        global boucl

        boucl = 0
        verp=0
        global dam
        dam=0


        while self.playing:
            self.check_events()
            if self.START_KEY:
                self.playing= True
            # injecter l'image sur l'écran pour appliquer l'arrière plan au jeu
            screen.blit(background, (x, 0))
            if cpt<0 and play==0:
                song2.stop()

                #pygame.mixer.Channel(3).play(pygame.mixer.Sound('SONS/potc.wav'))
                if arret==0:
                    song.play(-1)
                play=1
            if cpt>0:
                if vag2==1 or vag3==1 or vag4==1 or vag5==1:
                    song.stop()
                song2.play()
                play=0

            if cpt>0:  #Si cpt > 0, c'est à dire si l'écran déroule vers la droite, les cactus se repositionnent à droite de l'écran
                for cactus in game.all_monsters:
                    cactus.reposition()
                for cactus2 in game.cactus2.c2:
                    cactus2.reposition()
                for epines in game.player.all_projectiles:
                    epines.change(1)
                for cactus3 in game.cactus3.c3:
                    cactus3.reposition()
                for cactus4 in game.cactus4.c4:
                    cactus4.reposition()
                for cactus5 in game.cactus5.c5:
                    cactus5.reposition()

            if (vag2==1 or vag3==1 or vag4==1 or vag5==1) and cpt<0 :
                for cactus in game.all_monsters:
                    cactus.reposition()
                for cactus2 in game.cactus2.c2:
                    cactus2.reposition()
                for epines in game.player.all_projectiles:
                    epines.change(1)
                for cactus3 in game.cactus3.c3:
                    cactus3.reposition()
                for cactus4 in game.cactus4.c4:
                    cactus4.reposition()
                for cactus5 in game.cactus5.c5:
                    cactus5.reposition()
                #pour ne pas faire en sorte d'entrer à l'infini dans les conditions au dessus, on incrémente les vagues
                if vag2==1:
                    vag2+=1
                if vag3==1:
                    vag3+=1
                if vag4==1:
                    vag4+=1
                if vag5==1:
                    vag5+=1


            #Afficher les différents rounds en fonction de la vague
            if vag2<1 and cpt<0:
                    screen.blit(r11,(5,5))
            
            if vag2>1 and vag3<1:
                    screen.blit(r22,(5,5))

            if vag3>1 and vag4<1:
                    screen.blit(r33,(5,5))
            
            if vag4>1 and vag5<1:
                    screen.blit(r44,(5,5))
            
            if vag5>1:
                    screen.blit(r55,(5,5))
    
            if cpt<0:
                #Afficher les différentes icones en haut à droite une fois que l'écran va à gauche
                screen.blit(icone_bomb, (800,0))
                screen.blit(icone_pomp, (650,0))
                screen.blit(icone_cactus,(500,0))
                screen.blit(icone_bouclier,(950,0))
            for meteorite in game.player.all_projectiles:
                meteorite.move_bas()
            for bomb in game.player.all_projectiles:
                bomb.move_bas()

            for epines in game.player.all_projectiles:
                if vag5!=0:
                    ral=2
                if ral%2==0: #Trajectoire de l'épine (condition ral%2==0 pour la rendre plus lente)
                    if vag5<1:
                        epines.dessin(0,screen)
                    else:
                        epines.dessin(1,screen)
            if x>-1650 and cpt>0:
                #x=la position du fond désertique, pour faire bouger le désert derrière :
                x-=3
                verp=0
                cc=1
            else:
                cpt=-1

            #montrer l'arbre et la chouette
            game.groupe_arbre.arbre.draw(screen)
            game.groupe_chouette.chouette.draw(screen)
            for chouette in game.groupe_chouette.chouette:
                chouette.health_bar(screen)
            for bouclier in game.player.all_projectiles:
                bouclier.health_bar(screen)

            if cpt<0:
                #montrer les icones en haut à gauche
                screen.blit(music,(75,5))    
                screen.blit(n,(80,30))
                screen.blit(pause1,(130,5))
                screen.blit(p,(138,32))
                for cactus in game.all_monsters:
                    #faire avancer,sauter les cactus et montrer leur barre de vies
                    cactus.avancer(ver)
                    cactus.sauter()
                    cactus.update_health_bar(screen)
                    #Montrer les barres des attaques telles que le fusil à pompe etc.
                    cactus.special_bar(screen)
                    cactus.bomb_bar(screen, barre)
                    cactus.canon_bar(screen,barre2)
                    cactus.allie_bar(screen,barre3)
                    cactus.bouclier_bar(screen,barre4)
                    cactus.get_kill2()
                    #Change les cactus en fonction des vagues
                    if vag2==1:
                        cactus.meta(vag2,0,0,0)
                    if vag3==1:
                        cactus.meta(0,vag3,0,0)
                    if vag4==1:
                        cactus.meta(0,0,vag4,0)
                    if vag5==1:
                        cactus.meta(0,0,0,vag5)
                    ######

                for cactus2 in game.cactus2.c2:
                    #Memes commentaires que pour le boucle précédente
                    if vag5<1:
                        cactus2.avancer(ver)
                        cactus2.sauter()
                        cactus2.update_health_bar(screen)
                        if vag2 == 1:
                            cactus2.meta(vag2, 0, 0)
                        if vag3 == 1:
                            cactus2.meta(0, vag3, 0)
                        if vag4 == 1:
                            cactus2.meta(0, 0, vag4)
                for cactus3 in game.cactus3.c3:
                    if vag5<1:
                        cactus3.avancer(ver)
                        cactus3.sauter()
                        cactus3.update_health_bar(screen)
                        if vag2 == 1:
                            cactus3.meta(vag2, 0, 0)
                        if vag3 == 1:
                            cactus3.meta(0, vag3, 0)
                        if vag4 == 1:
                            cactus3.meta(0, 0, vag4)
                for cactus4 in game.cactus4.c4:
                    if vag5<1:
                        cactus4.avancer(ver)
                        cactus4.sauter()
                        cactus4.update_health_bar(screen)
                        if vag2 == 1:
                            cactus4.meta(vag2, 0, 0)
                        if vag3 == 1:
                            cactus4.meta(0, vag3, 0)
                        if vag4 == 1:
                            cactus4.meta(0, 0, vag4)
                for cactus5 in game.cactus5.c5:
                    if vag5<1:
                        cactus5.avancer(ver)
                        cactus5.sauter()
                        cactus5.update_health_bar(screen)
                        if vag2 == 1:
                            cactus5.meta(vag2, 0, 0)
                        if vag3 == 1:
                            cactus5.meta(0, vag3, 0)
                        if vag4 == 1:
                            cactus5.meta(0, 0, vag4)

            if ver2==1:
                for cactus_allie in game.player.all_projectiles:
                    #Faire avancer le cactus robot avec ar la direction dans laquelle va le cactus robot
                    cactus_allie.avancer2(ar)


            for balle in game.player.all_projectiles:
                balle.col2()
                balle.col()
                if temps >= 13:
                    #Après 13 tours de boucles, faire disparaitre la balle
                    balle.remove()
                if temps2 >= 5 :
                    #pareil
                    balle.remove_2()
            if cpt<0 and vag5<1:
                #Montrer les cactus si on n'est pas dans la derniere vague
                game.all_monsters.draw(screen)
                game.cactus2.c2.draw(screen)
                game.cactus3.c3.draw(screen)
                game.cactus4.c4.draw(screen)
                game.cactus5.c5.draw(screen)
            if vag5>=1 and cpt<0:
                #Montrer seulement le cactus 1 (qui devient le boss avec la fonction meta) si on est dans la vague 5 (la derniere)
                game.all_monsters.draw(screen)
            game.player.all_projectiles.draw(screen)
            
            if cpt<0:
                #Afficher la lunette de visée
                    screen.blit(game.player.image, game.player.rect)
            if cpt>=0:
                for bouclier in game.player.all_projectiles:
                    #Faire disparaitre le bouclier si l'écran va à droite à la fin d'un round
                    bouclier.damage(500)

            #Affichage des rounds en gros au milieu de l'écran à la fin d'une vague avec le son
            if vag2<1 and cpt>=0:
                    screen.blit(r1,(450,250))
                    if round1 == 0:
                        # son des rounds quand ils commencent (dans le même channel car les sons ne sont jamais entendus en même temps)
                        pygame.init()
                        pygame.mixer.pre_init()
                        pygame.mixer.init()
                        pygame.mixer.Channel(3).play(pygame.mixer.Sound('SONS/r1.wav'))
                        round1 += 1

            if vag2==1:
                   screen.blit(r2, (450,250))
                   if round2 == 0 :
                       pygame.init()
                       pygame.mixer.pre_init()
                       pygame.mixer.init()
                       pygame.mixer.Channel(3).play(pygame.mixer.Sound('SONS/r2.wav'))
                       round2 += 1
            if vag3==1:
                   screen.blit(r3, (450,250))
                   if round3 == 0:
                       pygame.init()
                       pygame.mixer.pre_init()
                       pygame.mixer.init()
                       pygame.mixer.Channel(3).play(pygame.mixer.Sound('SONS/r3.wav'))
                       round3 += 1
            if vag4==1:
                   screen.blit(r4, (450,250))
                   if round4 == 0:
                       pygame.init()
                       pygame.mixer.pre_init()
                       pygame.mixer.init()
                       pygame.mixer.Channel(3).play(pygame.mixer.Sound('SONS/r4.wav'))
                       round4 += 1
            if vag5==1:
                   screen.blit(r5, (450,250))
                   if fround == 0:
                       pygame.init()
                       pygame.mixer.pre_init()
                       pygame.mixer.init()
                       pygame.mixer.Channel(3).play(pygame.mixer.Sound('SONS/fr.wav'))
                       fround += 1

            #Passage d'une vague à une autre en fonction du nombre de cactus tués
            for cactus in game.all_monsters:
                if cactus.get_kill()==50 and vag2==0 :
                    cpt=1
                    vag2=1
                    ver=0
                    verp=0
                    cactus.modif_kill(0)
                if cactus.get_kill()==40 and vag3==0 and vag2>=1:
                    cpt=1
                    vag3=1
                    ver=0
                    verp=0
                    cactus.modif_kill(0)
                if cactus.get_kill()==30 and vag4==0 and vag3>=1 and vag2>=1:
                    cpt=1
                    vag4=1
                    ver=0
                    verp=0
                    cactus.modif_kill(0)
                if cactus.get_kill()==20 and vag5==0 and vag4>=1 and vag3>=1 and vag2>=1:
                    cpt=1
                    vag5=1
                    ver=0
                    verp=0
            # verifier si le joueur souhaite aller à gauche ou à droite en haut ou en bas et ne pas le faire sortir de la fenetre
            if game.pressed.get(pygame.K_RIGHT):
                if game.player.rect.x + game.player.rect.width < screen.get_width():
                    game.player.move_right()
            elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
                game.player.move_left()
            if game.pressed.get(pygame.K_UP) and game.player.rect.y > 0:
                game.player.move_up()
            elif game.pressed.get(pygame.K_DOWN) and game.player.rect.y + game.player.rect.height < screen.get_height():
                game.player.move_down()

            
            pygame.display.flip()
            # si le joueur ferme la fenetre
            # ctrl+ click droit sur get pour la liste des evenements que le joueur peut effectuer
            for event in pygame.event.get():
                # que l'evenement est fermeture de fenetre
                if event.type == pygame.QUIT:
                    # afin de fermer la fenetre
                    running = False
                    pygame.quit()
                    print("The Game has been closed.")
                    sys.exit()

                # detecter si le joueur utilise une touche du clavier
                elif event.type == pygame.KEYDOWN:
                    # La touche utilisée
                    game.pressed[event.key] = True
                    if event.key == pygame.K_SPACE:
                        # son quand l'utilisateur appuie pour tirer (en cliquant Espace) (dans le même channel que 'shotgun' car ils ne sont jamais utilsés en même temps)
                        pygame.mixer.Channel(1).play(pygame.mixer.Sound('SONS/cod.wav'))
                        game.player.launch_balle()
                        temps=0
                    if event.key == pygame.K_z:
                        if barre2>=100:
                            # son quand l'utilisateur utilise l'attaque 'shotgun' (en cliquant Z)
                            pygame.mixer.Channel(1).play(pygame.mixer.Sound('SONS/shotgun.wav'))
                            game.player.launch_balle_2()
                            barre2=0
                        temps2=0
                    if event.key == pygame.K_a:

                        if barre3>=100:
                            # son quand une attaque touche une cible
                            pygame.init()
                            pygame.mixer.pre_init()
                            pygame.mixer.init()
                            song3 = pygame.mixer.Sound('SONS/impact.wav')
                            song3.play()
                            game.player.launch_cactus()
                            barre3=0
                            ar+=1


                    if event.key == pygame.K_t:
                        for cactus in game.all_monsters:
                            if cpt<0 and temps3>=1000:
                                if self.cactus.check_kills(self.cactus):
                                    # son quand l'utilisateur utilise l'attaque 'missile géant' (touche T) (même channel que le petit missile car ils ne sont jamais utilsés en même temps)
                                    game.player.launch_meteorite()
                                    pygame.init()
                                    pygame.mixer.pre_init()
                                    pygame.mixer.init()
                                    pygame.mixer.Channel(2).play(pygame.mixer.Sound('SONS/grmissile.wav'))
                                    temps3=0
                                    cpt2=0
                    if event.key == pygame.K_r:
                        if barre4 == 100 and verp==1 and dam==0:
                            game.player.launch_bouclier()
                            game.player.launch_bouclier()
                            boucl = 1
                            dam=1
                            barre4=0
                    if event.key == pygame.K_e:
                        if barre>=100:
                            game.player.launch_bomb()
                            barre=0
                    if event.key == pygame.K_p and cpt<0 :
                            pause = True

                    if event.key == pygame.K_m and cpt<0:
                            song.stop()
                            #Algorithme pour qu'une fois le cactus robot va de gauche à droite, puis de droite à gauche, puis... en utilisant ar.
                            if arret==1:
                                song.play(-1)
                                arret=0
                                ar2=1
                            arret=1
                            if ar2==1:
                                arret=0
                                ar2=0
                elif event.type == pygame.KEYUP:
                    game.pressed[event.key] = False
                #pygame.draw.circle(screen,(111,102,104),((500,400)),10)
            
            
            while pause == True: #pause menu  On entre dans le menu pause
                #On affiche le menu et arrete la musique
                    screen.blit(pausemenu,(0,0))
                    song.stop()
                    pygame.display.flip()
                    for event in pygame.event.get():
                            if event.type == pygame.QUIT: #Faire quitter le jeu
                                    pygame.quit()
                                    sys.exit()

                            if event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_q:
                                            pygame.quit()
                                            sys.exit()

                                    if event.key == pygame.K_m:
                                            self.playing = False
                                            pause = False
                                            #song.play(-1)
                                    if event.key == pygame.K_p: #Mettre fin au menu pause
                                            pause = False
                                            if arret == 0 :
                                                song.play(-1)

            if x <= 0 and cpt<0 :
                x += 0.5
            if x==0 and cpt<0 :
                verp=1

            if cpt<0 and x>-169.5 and ral2%2==1:
                #Faire apparaitre l'arbre et la chouette progressivement une fois l'écran presque arrivé à gauche
                for arbre in game.groupe_arbre.arbre:
                    arbre.bougetoi()
                for chouette in game.groupe_chouette.chouette:
                    chouette.bougetoi2()
            if cpt>=0:
                for arbre in game.groupe_arbre.arbre:
                    arbre.reculetoi()
                for chouette in game.groupe_chouette.chouette:
                    chouette.reculetoi()

            if cc<3:
                if tE>250 and cc==1 and vag5<1:
                    game.player.launch_epine()
                    tE=0
                    cc+=1
                if tE2>450 and cc==2 and vag5<1:
                    game.player.launch_epine2()
                    tE2=0
                    cc+=1
            for mort in game.groupe_chouette.chouette:
                a = mort.death()

            #Faire tirer des épine à des moments et intervalles différents
            if vag5!=0 and ver==1:
                tE+=1
            if tE >= 700 + random.randint(100,700) and a!=1:
                game.player.launch_epine()
                tE=0
            if tE2 >= 700 + random.randint(100,700) and a!=1 and vag5<1:
                game.player.launch_epine2()
                tE2=0
            if tE3 >= 700 + random.randint(100,700) and a!=1 and vag5<1:
                game.player.launch_epine3()
                tE3=0
            if tE4 >= 700 + random.randint(100,700) and a!=1 and vag5<1:
                game.player.launch_epine4()
                tE4=0
            if tE5 >= 700 + random.randint(100,700) and a!=1 and vag5<1:
                game.player.launch_epine5()
                tE5=0
            if x==-270 and cpt<0:
                ver=1

            if cpt<0:
                #Faire augmenter la barre des attaques jusqu'à ce qu'elles se stabilisent à 100
                barre+=0.05
                if barre>=100:
                    barre=100
                barre2+=0.05
                if barre2>=100:
                    barre2=100
                barre3+=0.05
                if barre3>=100:
                    barre3=100
                if dam==0:
                    barre4+=0.05
                if barre4>=100:
                    barre4=100
            #des timers :
            temps+=1
            temps2+=1
            temps3+=1

            ral2+=1
            if ver==1:
                tE+=1
                tE2+=1
                tE3+=1
                tE4+=1
                tE5+=1
                ral+=1
            for cactus in game.all_monsters:
                b = cactus.fin()

            if dam==1:
                for bouclier in game.player.all_projectiles:
                    #Le bouclier prend des dégats automatiquement
                    bouclier.damage(0.2)

            while b==1: # quand on tue le boss final
                song.stop()
                screen.blit(win, (0, 0))
                pygame.display.flip()
                if congrats == 0:
                    # son quand l'utilisateur a fini le jeu (tous les rounds) et on le félicite gg (même channel que game over parce qu'ils ne sont jamais entendus en même temps)
                    pygame.init()
                    pygame.mixer.pre_init()
                    pygame.mixer.init()
                    pygame.mixer.Channel(6).play(pygame.mixer.Sound('SONS/congrats.wav'))
                    congrats += 1
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                            pygame.quit()
                            print("The Game has been closed.")
                            sys.exit()

                    if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_q:
                                    print('The Game has been closed.')
                                    pygame.quit()
                                    sys.exit()

                            if event.key == pygame.K_m:
                                    self.playing = False
                                    b = 0


            while  a==1 : # si la chouette meurt
                screen.blit(gameover, (x, 0))
                pygame.display.flip()
                song.stop()
                if gover == 0 :
                    # son quand l'utilisateur a perdu (la chouette est morte) ;(
                    pygame.init()
                    pygame.mixer.pre_init()
                    pygame.mixer.init()
                    pygame.mixer.Channel(6).play(pygame.mixer.Sound('SONS/gover.wav'))
                    gover += 1

                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                print("The Game has been closed.")
                                pygame.quit()
                                sys.exit()

                        if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_q:
                                        print('The Game has been closed.')
                                        pygame.quit()
                                        sys.exit()

                                if event.key == pygame.K_m:
                                        self.playing = False
                                        a = 0

    def check_events(self): # detecter les touches
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
                pygame.quit()
                sys.exit()
                
 
    def reset_keys(self): # r�initialiser les touches
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
 
    def draw_text(self, text, size, x, y ): # pour afficher du texte, avec couleur et taille...
        font = pygame.font.Font(self.font_name,size)
        text_surface = font.render(text, True, self.BROWN)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface,text_rect)

    #Différentes fonctions pour récupérer dans les autres fichiers, des variables globales
    def get_ar(self):
        global ar
        return ar

    def get_bouclier(self):
        global boucl
        return boucl

    def modif_bouclier(self,val):
        global boucl
        boucl = val

    def modif_dam(self,val):
        global dam
        dam = val

    def get_vag5(self):
        global vag5
        return vag5








        
   

