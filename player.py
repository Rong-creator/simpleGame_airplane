import pygame
from pygame.sprite import Sprite

class player(Sprite):
    def __init__(self) -> None:
        Sprite.__init__(self)
        self.image = pygame.Surface((50,40))
        self.image.fill((0,255,0))
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 400
    
    def update(self):
        self.rect.x += 2

