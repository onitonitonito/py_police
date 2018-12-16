"""-------------------------
# fuctions.py - 몸통에서 각 부속을 불러온다
#
#
#\n\n\n"""
print(__doc__)
import pygame


def set_image(filename):
    return pygame.image.load(filename)


def set_size(obj, width, height):
    return pygame.transform.scale(obj, (width, height))


def set_rotate(obj, angle):
    return pygame.transform.rotate(obj, angle)


def set_obj(obj_dict, key, rotate=0):
    """ MAKING IMAG_OBJ Using dict_key as OBJ_name """
    (size_x, size_y) = obj_dict[key][3]
    fname_wdir = obj_dict[key][0] + obj_dict[key][1]

    object = set_image(fname_wdir)
    object = set_size(object, size_x, size_y)
    object = set_rotate(object, rotate)
    return object


def draw_object(screen, object, posxy, rotate=0):
    (x, y) = posxy
    object = set_rotate(object, rotate)
    screen.blit(object, (x, y))


def draw_socre(screen, count):
    font = pygame.font.Font("freesansbold.ttf", 18)
    text = font.render(
        "Arrest Crime: {:}".format(count), True, (0, 255, 0))  # 00ff00
    screen.blit(text, (5, 10))


def draw_game_over(screen, pad_width, pad_height):
    font = pygame.font.Font("freesansbold.ttf", 38)
    text = font.render("GAME OVER", True, (255, 255, 255))  # ffffff

    text_pos = text.get_rect()
    text_pos.center = (pad_width / 2, pad_height * 0.45)

    screen.blit(text, text_pos)


def chk_key_event():
    for event in pygame.event.get():
        if event.type is pygame.QUIT:
            pygame.quit()
