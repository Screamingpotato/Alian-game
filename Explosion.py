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
        self.rect.move_ip(self.x_velocity, 0)

        if not self.SCREENRECT.contains(self.rect):
            self.x_velocity = -self.x_velocity

            self.rect.top = self.rect.bottom + 1
            self.rect = self.rect.clamp(self.SCREENRECT)

        self.frame = self.frame + 1
        self.image = self.images[self.frame//self.animation_cycle % 3]