import pygame
import json
from spritesheet import Spritesheet

#region ######################## Setup Game Window ######################################################

DISPLAY_W, DISPLAY_H = 720,480

window = pygame.display.set_mode((DISPLAY_W,DISPLAY_H))

#Setup a display surface, which is what we actual draw too (this is stored in memory)
screen = pygame.display.get_surface()

#change window name
pygame.display.set_caption("My Pygame game game")

#set game to running at start
running = True

#endregion ############################################################################################



#region ######################## Setup Sprites #########################################################


#Create player sprite object from spritesheet
playerScale = 2
mySpriteSheet = Spritesheet('res/roguelikeChar_transparent.png')
playerSprite = [mySpriteSheet.parse_sprite("player_bare_standing",playerScale)]
spriteIndex = 0


#endregion #########################################################################



#region ######################## GAME LOOP ########################################

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False #end the game

        if event.type == pygame.KEYDOWN:
            #region ##################### (input) Move the player ###########################
            if event.key == pygame.K_d:
                pass #todo move player right
            if event.key == pygame.K_a:
                pass #todo move player left
            if event.key == pygame.K_w:
                pass #todo move player up
            if event.key == pygame.K_s:
                pass #todo move player down
            #endregion ###############################################################



        #region ################### (draw) draw to screen ####################################
        screen.fill((200,164,128))

        #draw the player
        screen.blit(playerSprite[spriteIndex], (DISPLAY_W / 2, DISPLAY_H / 2))
        window.blit(screen,(0,0))
        pygame.display.update()
        #endregion


#endregion #################################################################################################