import pygame
from pygame.sprite import Sprite
import random

SCREEN_SIZE = (500,600)
class rock(Sprite):
    def __init__(self) -> None:
        Sprite.__init__(self)
        self.image = pygame.Surface((30,40))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0,SCREEN_SIZE[0] - self.rect.width)
        self.rect.y = random.randrange(-100,-40)
        self.speedy = random.randrange(2,10)
        self.speedx = random.randrange(-3,3)
    
    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx

        # check whether  out of scope, reset position
        if self.rect.top > SCREEN_SIZE[1]:
            self.rect.x = random.randrange(0,SCREEN_SIZE[0] - self.rect.width)
            self.rect.y = random.randrange(-100,-40)
            self.speedy = random.randrange(2,10)
            self.speedx = random.randrange(-3,3)
        
        if self.rect.left > SCREEN_SIZE[0] or self.rect.right < 0:
            self.rect.x = random.randrange(0,SCREEN_SIZE[0] - self.rect.width)
            self.rect.y = random.randrange(-100,-40)
            self.speedy = random.randrange(2,10)
            self.speedx = random.randrange(-3,3)