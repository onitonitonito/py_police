"""-------------------------
# 00.run_app.py - 몸통에서 각 부속을 불러온다
#
#
#\n\n\n"""
print(__doc__)

import pygame

from random import randint
from asset.config import *     # 따로 저장한 변수 불러옴
from asset.functions import *  # 함수정의 파트 불러옴


def main():
    """ INITIALIZE GAME """
    pygame.init()
    FPS_CLOCK = pygame.time.Clock()   # FPS_CLK.tick(FPS)

    SCREEN = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption(SCREEN_TITLE)

    POLICE, num_po = set_obj(OBJ_DICT, 'police')
    PLAYER, num_pl = set_obj(OBJ_DICT, 'player')

    index = -1
    speed = 5
    posx = int(PAD_WIDTH / 2)
    posy = 300

    while 1:
        if index > 6:
            index = 0
        else:
            index += 1

        if posx < 0:
            posx = PAD_WIDTH - 30
            posy = randint(170, 300)
        else:
            posx -= speed

        chk_key_event()

        # SCREEN.fill(BLUE)
        SCREEN.fill(DARKGRAY)

        draw_socre(SCREEN, count=posy)
        draw_game_over(SCREEN, PAD_WIDTH, PAD_HEIGHT)

        draw_object(SCREEN, POLICE[index - 0], (100, 100), rotate=45)
        draw_object(SCREEN, POLICE[index - 2], (140, 100), rotate=45)
        draw_object(SCREEN, POLICE[index - 4], (180, 100), rotate=45)
        draw_object(SCREEN, POLICE[index - 6], (220, 100), rotate=45)

        draw_object(SCREEN, PLAYER[0], (posx, posy), rotate=0)

        pygame.display.update()
        FPS_CLOCK.tick(FPS)


if __name__ == '__main__':
    main()
