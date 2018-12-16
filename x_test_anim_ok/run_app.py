"""-------------------------
# 01. MAIN -
# loc: x_test_anim_ok/run_app.py
#
#\n\n\n"""
print(__doc__)

import pygame

from _config import *
from _class import *


def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)

    my_sprite = MySprite(HEAD_ANIM_FILENAME)
    my_group = pygame.sprite.Group(my_sprite)

    while 1:
        # a must-have to preventing error
        for event in pygame.event.get():
            if event.type is pygame.QUIT:
                pygame.quit()

        screen.fill(BACKGROUND_COLOR)
        my_group.update()
        my_group.draw(screen)

        pygame.display.update()
        CLOCK.tick(10)


if __name__ == '__main__':
    main()
