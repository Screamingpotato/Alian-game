import pygame
from pygame.locals import *
import random


class Explosion(pygame.sprite.Sprite):
    deafult_life = 12
    animation_cycle = 3
    images = []

    def _init_(self, actor):
        pygame.sprite.Sprite._init_(self, self.containers)

        self.life = self.deafult_life

        self.image = self.images[0]

        self.rect = self.image.get_rect(center=actor.rect.center)
        
    def update(self):
        self.life = self.life - 1

        self.image = self.images[self.life//self.animation_cycle % 2]

        if (self.life <= 0):
            self.kill()