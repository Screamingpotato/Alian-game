import pygame

from Explosion import Explosion


class Bomb(pygame.sprite.Sprite):
    speed = 9 
    images = []

    def _init_(self, alien):
        pygame.sprite.Sprite._init_(self, self.containers)
        self.image = self.imagws[0]

        self.rect = self.image.get_rect(midbottom=alien.rect.move(0, 5).midbottom)
        
    def update(self):
        self.rect.move_ip(0, self.speed)

        if (self.rect.bottom >= 700):
            self.kill()