import pygame
import json
from direct.showbase.PythonUtil import union


class Spritesheet:
    def __init__(self, filename):
        self.filename = filename
        self.sprite_sheet = pygame.image.load(filename).convert()
        self.meta_data = self.filename.replace('png','json') #!!! json file must be same name as sprsheet
        try:
            with open(self.meta_data) as f:
                self.data = json.load(f)
            f.close() #close file
        except ValueError:
            print("!!Failed to open/load  json file for spritesheet!!")




    def get_sprite(self,x,y,w,h):
        sprite = pygame.Surface((w,h)) #create the sprite surface
        sprite.set_colorkey((0,0,0)) #mask out pure black
        sprite.blit(self.sprite_sheet,(0,0), (x,y,w,h)) #draw the surface
        return sprite


    def parse_sprite(self, name, scale):
        sprite = self.data['frames'][name]['frame']
        x, y, w, h = sprite["x"], sprite["y"], sprite["w"], sprite["h"]
        image = self.get_sprite(x,y,w,h)
        #scale image
        image = pygame.transform.scale(image, (w * scale, h * scale))
        return image