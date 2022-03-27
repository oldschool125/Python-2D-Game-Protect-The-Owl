from game import Game
from cactus import Cactus
import pygame
game = Game(Cactus)

# commande pour le BGM qui jouera tout le temps sauf si on fait pause

pygame.init()
pygame.mixer.pre_init()
pygame.mixer.init()

song = pygame.mixer.Sound('SONS/potc.wav')
 
while game.running:
    game.curr_menu.display_menu()
    game.game_loop()

