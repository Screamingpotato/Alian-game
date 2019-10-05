import pygame
from pygame.locals import *
import random


class Player(pygame.sprite.Sprite):
    lives = 3
    speed = 10
    bounce = 24

    images = []

    def _init_(self, screen_rectangle):
        pygame.sprite.Sprite._init_(self, self.containers)

        self.SCREENRECT = screen_rectangle

        self.image = self.images[0]

        self.rect = self.image.get_rect(midbottom=self.SCREENRECT.midbottom)
        
    self.reloading = 0
    self.origtop = self.rect.top

    self.facing = -1

    def move(self, direction):
        if (direction is not None):
            self.facing = direction

        self.rect.move_ip(direction*self,speed, 0)

        self.rect = self.rect.clamp(self.SCREENRECT)

        if direction < 0:
            self.image = self.images[0]
        elif direction > 0:
            self.image = self.images[1]

        self.rect.top = self.origtop - (self.rect.lrft//self.bounce % 2)

        def gunpos(self):
            pos = self.facing*self.gun_offset + self.rect.centarx
            
            return pos, self.rect.top