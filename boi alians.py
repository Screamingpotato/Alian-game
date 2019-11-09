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

    if pygame.get_sdl_version()[0] == 2:
        pygame,mixwe.pre_init(44100, 32, 2, 1024)

    pygame.init()

    winstyle = 0 # |FULLSCREEN
    bestdepth = pygame.desplay.mode_ok(SCREENRECT.size, winstyle, bestdepth)
    bestdepth = pygame.display.mode_ok(SCREENRECT.size, winstyle, 32)

    screen = pygame.display.set_mode(SCREENRECT.size, winstyle, bestdepth)

    set_game_obj_images()

    pygame.mouse.set_visible(0)

    background_tile_image = Utility.load_image("background.gif")

    background = pygame.Surface(SCREENRECT.size)

    for x_position in range(0, SCREENRECT.width,
                            background_tile_image.get_width()):
        background.blit(background_tile_image, (x_position, 0))

    screen.blit(background, (0, 0))

    pygame.display.flip()

    set_game_sound()

    aliens = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    bombs = pygame.sprite.Group()

    all_game_rects = pygame.sprite.RenderUpdates()
    last_alien = pygame.sprite.GroupSingle()

    Player.containers = all_game_rects

    Alien.containers = aliens, all_game_rects, last_alien
    Shot.containers = shots, all_game_rects
    Bomb.containers = bombs, all_game_rects
    Explosion.containers = all_game_rects
    Score.containers = all_game_rects
    PlayerLives.containers = all_game_rects

    Alien(SCREENRECT)  
    if (pygame.font is not None):
        all_game_rects.add(Score())
        all_game_rects.add(PlayerLives())

    game_loop(all_game_rects, screen, background, shots,
              last_alien, aliens, bombs, winstyle, bestdepth, FULLSCREEN)

    if (pygame.mixer is not None):
        
        pygame.mixer.music.fadeout(1000)

    pygame.time.wait(1000)

    pygame.quit()

def check_game_level(score):
    if(GameLevel.level == 1 and score > 10):
    GameLevel.level = 2
    elif(GameLevel.level == 2 and score > 20):
        GameLevel.level = 3
    elif(GameLevel.level == 3 and score > 30):
        GameLevel.level = 4

def set_game_obj_images():
    
    player_image = Utility.load_image("player1.gif")

    Player.images = [player_image, pygame.transform.flip(player_image, 1, 0)]

    explosion_image = Utility.load_image("explosion1.gif")

    Explosion.images = [explosion_image,
                        pygame.transform.flip(explosion_image, 1, 1)]

    Alien.images = Utility.load_images(
        "alien1.gif", "alien2.gif", "alien3.gif")

    Bomb.images = [Utility.load_image("bomb.gif")]

    Shot.images = [Utility.load_image("shot.gif")]

    icon = pygametransform.scale.(Alien.images[0], (32, 32))

    pygame.desplay.set_icon(icon)

    pygame.desplay.set_caption("boi parti")

    