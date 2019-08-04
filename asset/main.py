"""
# 함수들 모음
# 일단 대충 합쳐저 있는것 조각조각 찢어본다.
#
#\n\n\n"""
print(__doc__)

import pygame
from .config import *

"""  CALCULATE """


def draw_socre(count):
    global SCREEN
    font = pygame.font.Font("freesansbold.ttf", 20)
    text = font.render("Arrest Crime: " + str(count), True, WHITE)
    SCREEN.blit(text, (5, 10))


def draw_game_over():
    global SCREEN
    font = pygame.font.Font("freesansbold.ttf", 45)
    text = font.render("GAME OVER", True, WHITE)

    text_pos = text.get_rect()
    text_pos.center = (PAD_WIDTH / 2, PAD_HEIGHT * 0.45)

    SCREEN.blit(text, text_pos)


def set_image(filename):
    return pygame.image.load(filename)


def set_size(obj, width, height):
    return pygame.transform.scale(obj, (width, height))


def set_rotate(obj, angle):
    return pygame.transform.rotate(obj, angle)


def set_obj(dict_key, f_name_wdir, rotate=0):
    """ MAKING IMAG_OBJ Using dict_key as OBJ_name """
    size_x = OBJ_DICT[dict_key][1]
    size_y = OBJ_DICT[dict_key][0]

    obj_name = set_image(f_name_wdir)
    obj_name = set_size(obj_name, size_x, size_y)
    obj_name = set_rotate(obj_name, rotate)
    return obj_name


def draw_object(obj, x, y):
    global SCREEN
    SCREEN.blit(obj, (x, y))


if __name__ == '__main__':
    pass
