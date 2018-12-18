"""-------------------------
# 02.fuctions.py - 몸통에서 각 부속을 불러온다
#
#
#\n\n\n"""
print(__doc__)

import pygame


class MySprite(pygame.sprite.Sprite):
    def __init__(self):
        super(MySprite, self).__init__()
        # adding all the sprites to sprite DARKGRAY

        self.first_name = "jp_police_0.png"
        self.image_name = self.first_name[:-6]
        self.index = 0
        self.posx, self.posy = OBJ_POS
        self.width, self.height = OBJ_SIZE
        self.move = SPEED

        self.images = []

        for i in range(8):
            pygame.image.load(
                IMG_DIR + "{:}_{:}.png".format(
                    self.image_name,
                    i,
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
        self.imgae = self.images[self.index]
