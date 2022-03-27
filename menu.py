import pygame
import sys
import pygame
import os
 
class Menu():   
    def __init__(self, game): #initialiser les tailles, positions et le curseur
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 40, 40)
        self.offset = - 100
 
    def draw_cursor(self): #dessiner le curseur
        self.game.draw_text('=', 30, self.cursor_rect.x-75, self.cursor_rect.y)
 
    def blit_screen(self): #fonction qui nous permettra d'actualiser l'ecran rapidement
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()
 
class MainMenu(Menu):

    pygame.init()
    pygame.mixer.pre_init()
    pygame.mixer.init()
    song3 = pygame.mixer.Sound('SONS/potc.wav')
    def __init__(self, game): #initialiser les positions de ce qui est dans le main menu
        Menu.__init__(self, game)
        self.state = "Start"
        self.startx, self.starty = self.mid_w,320
        self.story0x, self.story0y = self.mid_w,360 
        self.story1x, self.story1y = self.mid_w,400 
        self.controlsx, self.controlsy = self.mid_w,440 
        self.creditsx, self.creditsy = self.mid_w, 480 
        self.quitx, self.quity = self.mid_w, 520 
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
 
    def display_menu(self): #afficher le main menu
        self.song3.play()
        self.run_display = True
        while self.run_display:
            #song = pygame.mixer.Sound('SONS/potc.wav')
            #song.play()
            #pygame.mixer.Channel(4).play(pygame.mixer.Sound('SONS/potc.wav'))
            self.game.check_events()
            self.check_input()
            carte = pygame.image.load("images/carte.jpg")
            carte = pygame.transform.scale(carte,(1080,720))
            self.game.display.blit(carte,(0,0))
            pygame.display.flip()
            pygame.display.update()
            self.game.draw_text('Protect The Owl', 80, 1080/2 , 100)
            self.game.draw_text('The Main Menu', 40, self.game.DISPLAY_W / 2, 200)
            self.game.draw_text("Start The Game", 35, self.startx, self.starty)
            self.game.draw_text("The Story In English", 35, self.story0x, self.story0y)
            self.game.draw_text("The Story In French", 35, self.story1x, self.story1y)
            self.game.draw_text("The Controls", 35, self.controlsx, self.controlsy)
            self.game.draw_text("The Credits", 35, self.creditsx, self.creditsy)
            self.game.draw_text("Quit The Game", 35, self.quitx, self.quity)
            self.draw_cursor()
            self.blit_screen()

 
 
    def move_cursor(self):  #bouger le curseur dans le main menu
        if self.game.DOWN_KEY:
            # son 'bip' à chaque fois que l'utilisateur appuie sur la flèche up/down/left/right
            pygame.init()
            pygame.mixer.pre_init()
            pygame.mixer.init()
            song2 = pygame.mixer.Sound('SONS/bip.wav')
            song2.play()

            if self.state == 'Start':
                self.cursor_rect.midtop = (self.story0x + self.offset, self.story0y)
                self.state = 'Story In English'
            elif self.state == 'Story In English':
                self.cursor_rect.midtop = (self.story1x + self.offset, self.story1y)
                self.state = 'Story In French'
            elif self.state == 'Story In French':
                self.cursor_rect.midtop = (self.controlsx + self.offset, self.controlsy)
                self.state = 'Controls'
            elif self.state == 'Controls':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Credits':
                 self.cursor_rect.midtop = (self.quitx + self.offset, self.quity)
                 self.state = 'Quit'
            elif self.state == 'Quit':
                 self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                 self.state = 'Start'

        elif self.game.UP_KEY:

            pygame.init()
            pygame.mixer.pre_init()
            pygame.mixer.init()
            song3 = pygame.mixer.Sound('SONS/bip.wav')
            song3.play()

            if self.state == 'Start':
                self.cursor_rect.midtop = (self.quitx + self.offset, self.quity)
                self.state = 'Quit'
            elif self.state == 'Quit':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.controlsx + self.offset, self.controlsy)
                self.state = 'Controls'
            elif self.state == 'Controls':
                self.cursor_rect.midtop = (self.story1x + self.offset, self.story1y)
                self.state = 'Story In French'
            elif self.state == 'Story In French':
                self.cursor_rect.midtop = (self.story0x + self.offset, self.story0y)
                self.state = 'Story In English'
            elif self.state== 'Story In English':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'


    def check_input(self): #detecter la position du curseur
        self.move_cursor()
        if self.game.START_KEY:
            # son quand l'utilisateur sélectionne ce qu'il souhaite dans le menu (touche entrée)
            pygame.init()
            pygame.mixer.pre_init()
            pygame.mixer.init()
            song = pygame.mixer.Sound('SONS/ok.wav')
            song.play()

            if self.state == 'Start':
                self.game.playing = True
                self.song3.stop()
            elif self.state == 'Story In English':
                self.game.curr_menu = self.game.story0
                self.song3.stop()
            elif self.state == 'Story In French':
                 self.game.curr_menu = self.game.story1
                 self.song3.stop()
            elif self.state == 'Controls':
                 self.game.curr_menu = self.game.controls
                 self.song3.stop()
            elif self.state == 'Credits':
                self.game.curr_menu = self.game.credits
                self.song3.stop()
            elif self.state == 'Quit':
                self.game.curr_menu = self.game.quit
                sys.exit()
            self.run_display = False
 
 

class Story0Menu(Menu): #tout ce qui est en rapport avec Story in English / affichage,sons...
    def __init__(self, game):
        Menu.__init__(self, game)
 
    def display_menu(self):
        self.run_display = True
        avengers = 0
        eng = 0
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY:

                pygame.init()
                pygame.mixer.pre_init()
                pygame.mixer.init()
                #song8 = pygame.mixer.Sound('SONS/ok.wav')
                #song8.play()
                pygame.mixer.Channel(4).play(pygame.mixer.Sound('SONS/ok.wav'))

                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            carte = pygame.image.load("images/carte.jpg")
            carte = pygame.transform.scale(carte,(1080,720))
            self.game.display.blit(carte,(0,0))
            pygame.display.flip()
            pygame.display.update()
            if avengers == 0 :
                # BGM quand on affiche les histoires en français ou anglais
                pygame.init()
                pygame.mixer.pre_init()
                pygame.mixer.init()
                song = pygame.mixer.Sound('SONS/avengers.wav')
                song.play(-1)
                song.set_volume(0.2)
                avengers += 1
            if eng == 0 :
                # histoire lue en anglais (mise plusieurs fois pour augmenter le son)
                pygame.init()
                pygame.mixer.pre_init()
                pygame.mixer.init()
                song2 = pygame.mixer.Sound('SONS/eng.wav')
                song3=pygame.mixer.Sound("SONS/eng.wav")
                song4=pygame.mixer.Sound("SONS/eng.wav")
                song5=pygame.mixer.Sound("SONS/eng.wav")
                song5.play()
                song2.play()
                song3.play()
                song4.play()
                eng =+ 1
            self.game.draw_text("The Game Story :", 40, self.game.DISPLAY_W / 2, 160)
            self.game.draw_text("Imagine yourself as a cactus, imagine yourself in one of their tribes, in which you are the one who is always ridiculed and humiliated, indeed you", 20, 1080/2 -6,220)
            self.game.draw_text("have no thorns and therefore no honor. Laash is the nickname they gave you. Your family abandoned you from the moment you were born and you", 20, 1080/2 + 3,240)
            self.game.draw_text("have no one to support you during the humiliations that take place every night, where you are planted with thorns in front of everyone. You", 20, 1080/2 - 4,260)
            self.game.draw_text("decide one evening to leave the village and never set foot there again. You walk for a long time in the desert, it is dark, it is very cold, the ", 20, 1080/2 - 9 ,280)
            self.game.draw_text("wind is blowing at full speed. It blows so hard that your roots leave the ground and you end up high in the air. You scream, you cry for help,", 20, 1080/2 - 10  ,300)
            self.game.draw_text("but the wind does not let it be heard. The ground is getting closer, you close your eyes not knowing if you will still be alive when you land,", 20, 1080/2 -11 ,320)
            self.game.draw_text("when suddenly some kind of flying beast catches you by the beak ... It's an owl! However it has a hard time supporting your weight in addition", 20, 1080/2 - 9 ,340)
            self.game.draw_text("to the wind, and it ends up crashing not far from your village, in the branches of a dead tree. You notice then that the wings of your friend", 20, 1080/2 -9 ,360)
            self.game.draw_text("the owl have broken. Something has to be done ! If we notice the presence of an owl, the tribes will rush on it to kill it, not tolerating the", 20, 1080/2 -4 ,380)
            self.game.draw_text("presence of intruders in their territory! You come down from the tree and secretly return to the village to take any weapons you can find.", 20, 1080/2 -8 ,400)
            self.game.draw_text("You then take a sniper rifle, a shotgun, a missile launcher, some cactus robots, and notice that there is a remote control to launch a huge", 20, 1080/2 -15 ,420)
            self.game.draw_text("missile in front of the village in the event of an invasion. What was bound to happen happened, the sun had not fully risen as all the tribes", 20, 1080/2 -11 ,440)
            self.game.draw_text("were already informed that a wounded owl was perched on a tree in the desert. You then go up on a mountain to gain height, you take with", 20, 1080/2 - 9 ,460)
            self.game.draw_text("you all your weapons. Now is the time to stand up for the owl that saved you and show them what you can do. ' I know if I fail I won't", 20, 1080/2 -20 ,480)
            self.game.draw_text("regret it, but I know that the only thing I will regret is not trying because at the end of the day I am HOPE. ' LAASH.", 20, 1080/2 -77 ,500)
            self.blit_screen()
        song.stop()
        song2.stop()
        song3.stop()
        song4.stop()
        song5.stop()


class Story1Menu(Menu): #tout ce qui est en rapport avec story in french / affichage, sons...
    def __init__(self, game):
        Menu.__init__(self, game)
 
    def display_menu(self):
        self.run_display = True
        avengers = 0
        fran = 0
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY:

                pygame.init()
                pygame.mixer.pre_init()
                pygame.mixer.init()
                #song8 = pygame.mixer.Sound('SONS/ok.wav')
                #song8.play()
                pygame.mixer.Channel(4).play(pygame.mixer.Sound('SONS/ok.wav'))

                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            carte = pygame.image.load("images/carte.jpg")
            carte = pygame.transform.scale(carte,(1080,720))
            self.game.display.blit(carte,(0,0))
            pygame.display.flip()
            pygame.display.update()

            if avengers == 0 :
                pygame.init()
                pygame.mixer.pre_init()
                pygame.mixer.init()
                song = pygame.mixer.Sound('SONS/avengers.wav')
                song.play(-1)
                song.set_volume(0.1)
                avengers += 1
            if fran == 0 :
                # histoire lue en français
                pygame.init()
                pygame.mixer.pre_init()
                pygame.mixer.init()
                song3 = pygame.mixer.Sound('SONS/fran.wav')
                song3.play()
                fran += 1
            self.game.draw_text("L'histoire Du Jeu :", 40, self.game.DISPLAY_W / 2, 160)
            self.game.draw_text("Imagine-toi en tant que cactus, imagine-toi dans une de leurs tribus, dans laquelle tu es celui qui est toujours ridiculise et humilie, tu n'as en ", 20, 1080/2 -8,220)
            self.game.draw_text("effet aucune epine et donc aucun honneur. Laash est le surnom qu'ils t'ont donne. Ta famille t'a abandonne des ta naissance et tu n'as personne  ", 20, 1080/2 -2,240)
            self.game.draw_text("pour te soutenir lors des humiliations qui ont lieu chaque soir, ou on te plante des epines devant tout le monde. Tu decides un soir de sortir du", 20, 1080/2 - 6,260)
            self.game.draw_text("village et de ne plus jamais y remettre les pieds. Tu marches longtemps dans le desert, il fait nuit, il fait tres froid, le vent souffle a toute", 20, 1080/2 - 5 ,280)
            self.game.draw_text("allure. Il souffle si fort que tes racines quittent le sol et que tu te retrouves tres haut dans les airs. Tu pousses des cris, tu appelles a l'aide ", 20, 1080/2  ,300)
            self.game.draw_text("mais le vent ne laisse rien entendre. Le sol se rapproche, tu fermes les yeux ne sachant pas si tu seras encore en vie a l'atterrissage, quand", 20, 1080/2 - 23  ,320)
            self.game.draw_text("soudainement une sorte de bete volante te rattrape avec son bec... C'est une chouette ! Elle a cependant beaucoup de mal a supporter ton poids", 20, 1080/2 -1  ,340)
            self.game.draw_text("en plus du vent et elle finit par s'ecraser pas loin de ton village, dans les branches d'un arbre mort. Tu remarques alors que les ailes de ton amie", 20, 1080/2 + 3 ,360)
            self.game.draw_text("la chouette se sont cassees. Il faut faire quelque chose ! Si on remarque la presence d'une chouette, les tribus vont se ruer dessus pour la tuer", 20, 1080/2 - 7 ,380)
            self.game.draw_text("ne tolerant pas la presence d'intrus sur leur territoire ! Tu descends de l'arbre et rentres secretement au village prendre toutes les armes que", 20, 1080/2 +1 ,400)
            self.game.draw_text("tu trouves. Tu prends alors un fusil a lunette, un fusil a pompe, un lance-missiles, des robots cactus, et tu remarques qu'il y a une telecommande", 20, 1080/2 +5 ,420)
            self.game.draw_text("permettant de lancer un enorme missile devant le village en cas d'invasion. Ce qui devait arriver arriva, le soleil ne s'etait pas completement", 20, 1080/2 - 11 ,440)
            self.game.draw_text("leve que toutes les tribus etaient deja tenues au courant qu'une chouette blessee etait posee sur un arbre dans le desert. Tu montes alors une", 20, 1080/2 -3 ,460)
            self.game.draw_text("montagne pour prendre de la hauteur, tu prends avec toi toutes tes armes. C'est le moment de defendre la chouette qui t'a sauve et de leur", 20, 1080/2 -13 ,480)
            self.game.draw_text("montrer ce que tu sais faire. ' Je sais que si j'echoue, je ne le regretterai pas, mais je sais que la seule chose que je pourrai regretter est de ne", 20, 1080/2 -4 ,500)
            self.game.draw_text("pas essayer car en definitive je suis l'ESPOIR. ' LAASH.", 20, 1080/2 - 327 ,520)
            self.blit_screen()
        song.stop()
        song3.stop()






class ControlsMenu(Menu): # l'affichage du texte pour controls 
    def __init__(self, game):
        Menu.__init__(self, game)
 
    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY:

                pygame.init()
                pygame.mixer.pre_init()
                pygame.mixer.init()
                #song8 = pygame.mixer.Sound('SONS/ok.wav')
                #song8.play()
                pygame.mixer.Channel(4).play(pygame.mixer.Sound('SONS/ok.wav'))

                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            carte = pygame.image.load("images/carte.jpg")
            carte = pygame.transform.scale(carte,(1080,720))
            self.game.display.blit(carte,(0,0))
            pygame.display.flip()
            pygame.display.update()
            self.game.draw_text('The Controls', 80, self.game.DISPLAY_W / 2, 100)
            self.game.draw_text('A : Cactus Robot', 35, self.game.DISPLAY_W / 2, 200)
            self.game.draw_text('Z : Shotgun', 35, self.game.DISPLAY_W / 2, 240)
            self.game.draw_text('E : Small Missile', 35, self.game.DISPLAY_W / 2, 280)
            self.game.draw_text('R : Shield', 35, self.game.DISPLAY_W / 2, 320)
            self.game.draw_text('T : Giant Missile', 35, self.game.DISPLAY_W / 2, 360)
            self.game.draw_text('P : Pause/UnPause ', 35, self.game.DISPLAY_W / 2, 400)
            self.game.draw_text('M : Music On/Off', 35, self.game.DISPLAY_W / 2, 440)
            self.game.draw_text('Space Bar : Shoot', 35, self.game.DISPLAY_W / 2, 480)
            self.game.draw_text('Directional Keys : Move the Scope', 35, self.game.DISPLAY_W / 2, 520)
            self.blit_screen()



class CreditsMenu(Menu): # l'affichage du texte pour credits
    def __init__(self, game):
        Menu.__init__(self, game)
 
    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY:

                pygame.init()
                pygame.mixer.pre_init()
                pygame.mixer.init()
                #song8 = pygame.mixer.Sound('SONS/ok.wav')
                #song8.play()
                pygame.mixer.Channel(4).play(pygame.mixer.Sound('SONS/ok.wav'))

                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            carte = pygame.image.load("images/carte.jpg")
            carte = pygame.transform.scale(carte,(1080,720))
            self.game.display.blit(carte,(0,0))
            pygame.display.flip()
            pygame.display.update()
            self.game.draw_text('Credits', 80, self.game.DISPLAY_W / 2,100)
            self.game.draw_text('Game by LAASH', 40, (self.game.DISPLAY_W / 2)+200, 200)
            self.game.draw_text('Other Credits', 40, (self.game.DISPLAY_W / 2)-200, 200)
            self.game.draw_text('Images : Flaticon', 35, (self.game.DISPLAY_W / 2)-200, 320)
            self.game.draw_text('Lorie LUC', 35, (self.game.DISPLAY_W / 2)+200, 320)
            self.game.draw_text('          Freepik', 35, (self.game.DISPLAY_W / 2)-200, 360)
            self.game.draw_text('Music : The Warp Zone', 35, (self.game.DISPLAY_W / 2)-200, 400)
            self.game.draw_text('         Gizmafy', 35, (self.game.DISPLAY_W / 2)-200,440)
            self.game.draw_text('         Drix Gaming', 35, (self.game.DISPLAY_W / 2)-200, 480)
            self.game.draw_text('Anass OBEIDAT', 35, (self.game.DISPLAY_W / 2)+200, 360)
            self.game.draw_text('Adam TORJMAN', 35, (self.game.DISPLAY_W / 2)+200, 400)
            self.game.draw_text('Sulaiman-Sajid FAYYAZ ', 35, (self.game.DISPLAY_W / 2)+200,440)
            self.game.draw_text('Haytam EL HILALI', 35, (self.game.DISPLAY_W / 2)+200, 480)

            self.blit_screen()
class QuitMenu(Menu): #ce qui nous permet de quitter en mettant ENTRER dans le main menu
    def quit_menu(self):
        if self.game.START_KEY:

            pygame.init()
            pygame.mixer.pre_init()
            pygame.mixer.init()
            #song9 = pygame.mixer.Sound('SONS/ok.wav')
            #song9.play()
            pygame.mixer.Channel(5).play(pygame.mixer.Sound('SONS/ok.wav'))

            if self.state == 'Quit':
                pygame.quit()
                sys.exit()
                print("The Game has been closed.")



















