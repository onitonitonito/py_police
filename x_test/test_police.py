"""
# test_police.py - 몸통에서 각 부속을 불러온다
#
#\n\n\n"""
print(__doc__)
# File "main.py", line 20, in draw_socre()
# text = font.render("Arrest Crime: "+str(count), True, FONT_COLOR)
#     -- NameError: name 'FONT_COLOR' is not defined

import sys
import time
import pygame

from asset.config import *         # 따로 저장한 변수를 불러온다.
# from asset.main import *           # 2개 이상 불러올 때 문제가...있다


"""  CALCULATE """
def draw_socre(count):
    global DISPLAYSURF
    font = pygame.font.Font("freesansbold.ttf", 20)
    text = font.render("Arrest Crime: "+ str(count), True, FONT_COLOR)
    DISPLAYSURF.blit(text, (5, 10))



if __name__ == '__main__':
    """ INITIALIZE GAME """
    pygame.init()

    DISPLAYSURF = pygame.display.set_mode((PAD_WIDTH, PAD_HEIGHT))
    pygame.display.set_caption('HEY.........TEST!!!')
    FPS_CLK = pygame.time.Clock()   # FPS_CLK.tick(FPS)

    x = PAD_WIDTH * 0.45                          # 45% 플레이어 pos_x
    y = PAD_HEIGHT * 0.80 - (PLAYER_HEIGHT * 1.7)  # 80% 플레이어 pos_y

    ongame = True                   # 루프를 빠져나가기 위한 옵션
    anim = 0                        # 아니메 스프라이트 8장 카운트를 위한 숫자

    while ongame:
        DISPLAYSURF.fill(GREEN)

        # 패드폭 안에 있으면 마이너스 해서 리턴한다.
        if ENEMY_WIDTH < EPOS_X < PAD_WIDTH - ENEMY_WIDTH:
            EPOS_X -= EPOS_MOV
        else:
            EPOS_X = PAD_WIDTH - (1.5 * ENEMY_WIDTH)

        draw_socre(120)

        pygame.display.update()
        FPS_CLK.tick(FPS)
        time.sleep(0.1)
