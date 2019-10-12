import random 
import os.path

import pygame
from pygame.locals import Rect, Quit, KEYDOWN, K_RIGHT, K_LEFT, K_SPACE, \
    K_ESCAPE, FULLSCREEN
from alian import Alien
from Bomb import Bomb
from Explosion import Explosion
from player import player 
from playerlives import playerlives
from Scoer import Scoer
from Shot import Shot
import utility

if not pygame.image.get_extended():
    raise SystemExit("Sorry, extended image modulerequired")

MAX_SHOTS = 2 
ALIEN_ODDS = 22
BOMB_ODDS = 12
ALIEN_RELOAD = 12

SCREENRECT = Rect(0, 0, 1024, 768)
main_directory = os.path.split(os.path.abspath (__file__))[0]

def main(winstyle=0):
    pass