import pygame
import json
from spritesheet import Spritesheet




DISPLAY_W, DISPLAY_H = 720,480

window = pygame.display.set_mode((DISPLAY_W,DISPLAY_H))

#Setup a display surface, which is what we actual draw too (this is stored in memory)
screen = pygame.display.get_surface()

#change window name
pygame.display.set_caption("My Pygame game game")

#set game to running at start
running = True

#setup game speed
clock = pygame.time.Clock()




#player class
#TODO: create player class
class Player:
    """
    Spawn a player
    """
    def __init__(self, x, y):
        self.speed = .1


        self.rect = pygame.Rect(x, y, 16, 16)
        self.x = x
        self.y = y
        self.velX = 0
        self.velY = 0
        #input checks
        self.left_pressed   = False
        self.right_pressed  = False
        self.up_pressed     = False
        self.down_pressed   = False

        #Create player sprite object from spritesheet
        self.playerScale    = 2
        self.mySpriteSheet  = Spritesheet('res/roguelikeChar_transparent.png')
        self.playerSprite   = [self.mySpriteSheet.parse_sprite("player_bare_standing",self.playerScale)]
        self.spriteIndex    = 0



    def draw(self, surface):
        surface.blit(self.playerSprite[self.spriteIndex], (self.x, self.y))

    def update(self):
        self.velX = 0 #reset
        self.velY = 0 #reset
        if self.left_pressed and not self.right_pressed:
            self.velX = -self.speed
        if self.right_pressed and not self.left_pressed:
            self.velX = self.speed
        if self.up_pressed and not self.down_pressed:
            self.velY = -self.speed
        if self.down_pressed and not self.up_pressed:
            self.velY = self.speed

        #move to mouse pos


        self.x += self.velX
        self.y += self.velY

        #set the player rectangle on the player
        self.rect =  pygame.Rect(self.x, self.y, 16, 16)




#initialize the player
player = Player(DISPLAY_W / 2, DISPLAY_H / 2)


#test collision rectangle
test_rect = pygame.Rect(100, 100, 400, 100)


while running:
    screen.fill((0,0,0))


    #draw
    player.draw(screen)


    if player.rect.colliderect(test_rect):
        pygame.draw.rect(screen, (255,0,0),test_rect)
    else:
        pygame.draw.rect(screen, (32,32,32), test_rect)


    #update
    pygame.display.update()
    player.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False #end the game

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player.right_pressed = True
            if event.key == pygame.K_LEFT:
                player.left_pressed = True
            if event.key == pygame.K_UP:
                player.up_pressed = True
            if event.key == pygame.K_DOWN:
                player.down_pressed = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                player.right_pressed = False
            if event.key == pygame.K_LEFT:
                player.left_pressed = False
            if event.key == pygame.K_UP:
                player.up_pressed = False
            if event.key == pygame.K_DOWN:
                player.down_pressed = False

        #debug, click to move
        mousePos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            player.x = mousePos[0]
            player.y = mousePos[1]



        clock.tick(60)

