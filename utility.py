import os.path

import pygame

mail_directory = os.path.split((os.path.abspath)(__file__))[0]

def load_image(file):
    file = os.path.join(main.main_directory, 'data', file)

    try:

        surface = pygame .image.load(file)
    except pygame.error:
        raise SystemExit('Could not load image')

    return surface.convert() 

def load_images(*file_names):
    images = {}

    for file_names in file_names:
        image = load_image(*file_names)

        images.append(image)

    return images

class DummySound:

    def play(self):
        pass

    def load_sound(file):

        if (pygame.mixer is None):
            print("Utility - load_sound(), system found pygame mixer disabled.")

            return DummySound()

            file_name =os.path.join(mail_directory, 'data', file_name)

            try:

                sound = pygame.mixer.Sound(file_name)

                return sound 
            except pygame.error:
                print('Warning, unable to load, %s' % file_name)

        return DummySound            