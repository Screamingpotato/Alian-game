    """
        Simple DirectMedia Layer (SDL) is a cross-platform development \
        library designed to provide low level access to audio, keyboard, \
        mouse, joystick, and graphics hardware via OpenGL and Direct3D. It \
        is used by video playback software, emulators, and popular games
    """

    # Initialize pygame
    if pygame.get_sdl_version()[0] == 2:
        pygame.mixer.pre_init(44100, 32, 2, 1024)

    pygame.init()

    # Set the display mode
    # will go to full screen if uncommented
    winstyle = 0  # |FULLSCREEN

    # checks whether display mode is available
    bestdepth = pygame.display.mode_ok(SCREENRECT.size, winstyle, 32)

    # This function will create a display Surface
    # Initialize a window or screen for display
    screen = pygame.display.set_mode(SCREENRECT.size, winstyle, bestdepth)

    set_game_obj_images()

    # hide the mouse cursor
    pygame.mouse.set_visible(0)

    # create the background, tile the background image
    background_tile_image = Utility.load_image("background.gif")

    background = pygame.Surface(SCREENRECT.size)

    for x_position in range(0, SCREENRECT.width,
                            background_tile_image.get_width()):
        background.blit(background_tile_image, (x_position, 0))

    # Draws a source Surface onto this Surface
    screen.blit(background, (0, 0))

    # Update the full display Surface to the screen
    pygame.display.flip()

    # game sound enabled
    set_game_sound()

    # TODO: Initialize game states
    # states = [PlayGameState(),OptionsState(),GameOverState()]

    # Initialize Game Groups
    # The Group class is just a simple container
    aliens = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    bombs = pygame.sprite.Group()

    # a list of pygame Rects, representing all areas
    # changed on the screen
    all_game_rects = pygame.sprite.RenderUpdates()
    last_alien = pygame.sprite.GroupSingle()

    # assign default groups to each sprite class
    Player.containers = all_game_rects

    Alien.containers = aliens, all_game_rects, last_alien
    Shot.containers = shots, all_game_rects
    Bomb.containers = bombs, all_game_rects
    Explosion.containers = all_game_rects
    Score.containers = all_game_rects
    PlayerLives.containers = all_game_rects

    Alien(SCREENRECT)  # note, this "lives" because it goes into a sprite group

    if (pygame.font is not None):
        all_game_rects.add(Score())
        all_game_rects.add(PlayerLives())

    game_loop(all_game_rects, screen, background, shots,
              last_alien, aliens, bombs, winstyle, bestdepth, FULLSCREEN)

    # quit game
    # if pygame sound is running
    if (pygame.mixer is not None):
        # for 1 second = 1000 milliseconds
        pygame.mixer.music.fadeout(1000)

    pygame.time.wait(1000)

    pygame.quit()


def set_game_obj_images():
    # Load images, assign to sprite classes
    # (do this before the classes are used, after screen setup)
    player_image = Utility.load_image("player1.gif")

    # 2 images: tank facing left, tank facing right
    Player.images = [player_image, pygame.transform.flip(player_image, 1, 0)]

    explosion_image = Utility.load_image("explosion1.gif")

    # only 2 images!  just flipping the image to create 2nd
    Explosion.images = [explosion_image,
                        pygame.transform.flip(explosion_image, 1, 1)]

    Alien.images = Utility.load_images(
        "alien1.gif", "alien2.gif", "alien3.gif")

    Bomb.images = [Utility.load_image("bomb.gif")]
