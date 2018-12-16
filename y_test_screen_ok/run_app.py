"""-------------------------
# run_app.py - 몸통에서 각 부속을 불러온다
#
#
#\n\n\n"""
print(__doc__)

import sys
import time
import pygame

from asset.config import *     # 따로 저장한 변수 불러옴
from asset.functions import *  # 함수정의 파트 불러옴




def main():
    """ INITIALIZE GAME """
    pygame.init()

    SCREEN = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption(SCREEN_TITLE)


    FPS_CLOCK = pygame.time.Clock()   # FPS_CLK.tick(FPS)

    POLICE = set_obj(OBJ_DICT, 'police')
    PLAYER = set_obj(OBJ_DICT, 'player')

    while 1:
        chk_key_event()

        SCREEN.fill(DARKGRAY)

        draw_socre(SCREEN, 120)
        draw_game_over(SCREEN, PAD_WIDTH, PAD_HEIGHT)

        draw_object(SCREEN, POLICE, (100, 100), rotate=45)
        draw_object(SCREEN, POLICE, (150, 100), rotate=45)
        draw_object(SCREEN, PLAYER, (100, 300), rotate=90)

        pygame.display.update()
        FPS_CLOCK.tick(FPS)




if __name__ == '__main__':
    main()
