import pygame
from pygame.sprite import Sprite

# the size of screen should be be put in here. A GLOBAL SETTING file is needed. 
SCREEN_SIZE = (500,600)

class player(Sprite):
    def __init__(self) -> None:
        Sprite.__init__(self)
        self.image = pygame.Surface((50,40))
        self.image.fill((0,255,0))
        self.rect = self.image.get_rect()
        # could load these constant seeting in a file

        self.rect.center = SCREEN_SIZE[0]/2, SCREEN_SIZE[1]/2
        self.speed_x = 8
    
    # update the detail of image per frame
    def update(self):
        key_pressed = pygame.key.get_pressed()
        # if the right button is pressed, let the plant move right side 
        if key_pressed[pygame.K_RIGHT]:
            self.rect.x += self.speed_x

        # if the left button is pressed, let the plant move left side 
        if key_pressed[pygame.K_LEFT]:
            self.rect.x -= self.speed_x

        # test whether out of scope
        if self.rect.right > SCREEN_SIZE[0]:
            self.rect.right = SCREEN_SIZE[0]
        
        if self.rect.right < 50 :
            self.rect.right = 50



