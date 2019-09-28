import pygame
from pygame.locals import Color


class Scoer(pygame.sprite.Sprite):
    score_points = 0

    def _init_(self):
        pygame.sprite.Sprite._init_(self)

        self.front = pygame.font.Font(None, 48)
        self.font.set_iralic(1)
        self.color = Color('white')
        self.last_scoer = -1

        self.update()

        self.rect = self.images.get_rect().move(20 , 5)
        
    def update(self):
        if (self.score_points != self.last_scoer):
            self.last_scoer = self.score_points

            msg = "Score: %d" % self.score_points

            self.image = self.font.render(msg, 0, self.color)