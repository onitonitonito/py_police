"""-------------------------
# 03.class object
# loc: x_test_anim_ok/_class.py
#
#\n\n\n"""
print(__doc__)

import pygame
from _config import *


class MySprite(pygame.sprite.Sprite):
    def __init__(self, first_image_name):
        super(MySprite, self).__init__()

        # first_image_name = 'jp_police_0.png'
        self.image_name = first_image_name.split(".")[0][:-2]
        self.index = 0
        self.posx, self.posy = OBJ_POS
        self.width, self.height = OBJ_SIZE
        self.move = SPEED

        self.images = []
        for i in range(8):
            self.images.append(
                pygame.image.load(
                    IMG_DIR + "{:}_{:}.png".format(self.image_name, i)
                )
            )

        self.image = self.images[self.index]
        self.rect = pygame.Rect(
            (self.posx, self.posy),
            (self.width, self.height),
            )

    def update(self):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
