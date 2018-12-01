"""
# 경찰차 애니매이션 - 총 8장의 스프라이트
# 오브젝트 딕트와 리스트가 막 뒤죽박죽 됬는데 .. 일단은 놔두고
# 천천히 리펙토링을 해야겠다~ 지금은 여기서 끝!
#
#\n\n\n"""
print(__doc__)

import sys
import time
import pygame
from asset.config import *         # 따로 저장한 변수를 불러온다.


"""  CALCULATE """
def draw_socre(count):
    global DISPLAYSURF
    font = pygame.font.Font("freesansbold.ttf", 20)
    text = font.render("Arrest Crime: "+ str(count), True, WHITE)
    DISPLAYSURF.blit(text, (5, 10))

def draw_game_over():
    global DISPLAYSURF
    font = pygame.font.Font("freesansbold.ttf", 45)
    text = font.render("GAME OVER", True, WHITE)

    text_pos = text.get_rect()
    text_pos.center = (PAD_WIDTH/2, PAD_HEIGHT*0.45)

    DISPLAYSURF.blit(text, text_pos)

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
    global DISPLAYSURF
    DISPLAYSURF.blit(obj, (x, y))

player = set_obj('player', DESTIN_DIR+'car_top.png', rotate=90 )
enemy = set_obj('enemy', DESTIN_DIR+'kr_police_0.png', rotate=0)

""" # 애니메이션을 불러온다.. 이게 좋은방법은 아니지만; 일단 한다. """
# 좋은 방법은 나중에 생각한다.. 리팩터링은 나중에 한가할 때, 인터넷 검색!
p_rotate = 45
pcars = {
    'pcar_0' : set_obj('enemy', DESTIN_DIR+'kr_police_0.png', p_rotate),
    'pcar_1' : set_obj('enemy', DESTIN_DIR+'kr_police_1.png', p_rotate),
    'pcar_2' : set_obj('enemy', DESTIN_DIR+'kr_police_2.png', p_rotate),
    'pcar_3' : set_obj('enemy', DESTIN_DIR+'kr_police_3.png', p_rotate),
    'pcar_4' : set_obj('enemy', DESTIN_DIR+'kr_police_4.png', p_rotate),
    'pcar_5' : set_obj('enemy', DESTIN_DIR+'kr_police_5.png', p_rotate),
    'pcar_6' : set_obj('enemy', DESTIN_DIR+'kr_police_6.png', p_rotate),
    'pcar_7' : set_obj('enemy', DESTIN_DIR+'kr_police_7.png', p_rotate),
    }

e_rotate = 0
ecars = {
    'ecar_0' : set_obj('enemy', DESTIN_DIR+'jp_police_0.png', e_rotate),
    'ecar_1' : set_obj('enemy', DESTIN_DIR+'jp_police_1.png', e_rotate),
    'ecar_2' : set_obj('enemy', DESTIN_DIR+'jp_police_2.png', e_rotate),
    'ecar_3' : set_obj('enemy', DESTIN_DIR+'jp_police_3.png', e_rotate),
    'ecar_4' : set_obj('enemy', DESTIN_DIR+'jp_police_4.png', e_rotate),
    'ecar_5' : set_obj('enemy', DESTIN_DIR+'jp_police_5.png', e_rotate),
    'ecar_6' : set_obj('enemy', DESTIN_DIR+'jp_police_6.png', e_rotate),
    'ecar_7' : set_obj('enemy', DESTIN_DIR+'jp_police_7.png', e_rotate),
    }





if __name__ == '__main__':
    """ INITIALIZE GAME """
    pygame.init()

    DISPLAYSURF = pygame.display.set_mode((PAD_WIDTH, PAD_HEIGHT))
    pygame.display.set_caption('GET IT CRIME!!')
    FPS_CLK = pygame.time.Clock()   # FPS_CLK.tick(FPS)

    x = PAD_WIDTH * 0.45                          # 45% 플레이어 pos_x
    y = PAD_HEIGHT * 0.80 - (PLAYER_HEIGHT * 1.7)  # 80% 플레이어 pos_y

    ongame = True                   # 루프를 빠져나가기 위한 옵션
    anim = 0                        # 아니메 스프라이트 8장 카운트를 위한 숫자

    while ongame:
        DISPLAYSURF.fill(BLACK)

        draw_socre(anim)
        draw_game_over()
        draw_object(player, x, y)

        # 아니메 카운터를 위한 숫자
        if anim < 7:
            anim += 1
        else:
            anim = 0


        # 패드폭 안에 있으면 마이너스 해서 리턴한다.
        if ENEMY_WIDTH < EPOS_X < PAD_WIDTH - ENEMY_WIDTH:
            EPOS_X -= EPOS_MOV
        else:
            EPOS_X = PAD_WIDTH - (1.5 * ENEMY_WIDTH)


        # 경찰차1,2,3 애니매이션
        draw_object(ecars['ecar_'+str(anim)], EPOS_X, EPOS_Y)
        draw_object(pcars['pcar_'+str(anim)], 300, 400)
        draw_object(pcars['pcar_'+str(anim)], 260, 390)

        pygame.display.update()
        FPS_CLK.tick(FPS)
        time.sleep(0.1)
