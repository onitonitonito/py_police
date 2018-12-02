"""
# Config.py - 의존성이 없는 독립 모듈을 만들어보자
#
#\n\n\n"""
print(__doc__)


import os

FPS = 30
WORK_DIR = os.path.dirname(__file__)
ROOT_WORD = 'x_test'                 # root directory
ROOT_DIR = WORK_DIR.partition(ROOT_WORD)[0] + WORK_DIR.partition(ROOT_WORD)[1]

DESTIN_DIR = os.path.join(ROOT_DIR, 'asset', 'img') + "\\"



""" # COLOR TABLE """
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


"""# 스크린 환경설정 변수"""
FONT_COLOR = BLACK


""" # 패드 사이즈 """
PAD_WIDTH = 480
PAD_HEIGHT = 640


"""# 에너미 위치"""
EPOS_X = 100
EPOS_Y = 150
EPOS_MOV = 8      # 움직이는 거리(속도)




"""# 스프라이트 오브젝트 정보"""
# 오브젝트 사전의 목적을 명확하게, 스프라이트 정보형상 ... 다시 정의
# 'key_name' :  [size_x, y, POS_x, y,'file_name.png'],
OBJ_DICT = {
        'player': [20, 30, 100, 100,'car_top.png'],
        'enemy' : [25, 30, 200, 200,'police_0.png'],

        'pcar_0' : [25, 30, 200, 200,'kr_police_0.png'],
        'pcar_1' : [25, 30, 200, 200,'kr_police_1.png'],
        'pcar_2' : [25, 30, 200, 200,'kr_police_2.png'],
        'pcar_3' : [25, 30, 200, 200,'kr_police_3.png'],
        'pcar_4' : [25, 30, 200, 200,'kr_police_4.png'],
        'pcar_5' : [25, 30, 200, 200,'kr_police_5.png'],
        'pcar_6' : [25, 30, 200, 200,'kr_police_6.png'],
        'pcar_7' : [25, 30, 200, 200,'kr_police_7.png'],
    }

# 도망차 -- 어두운 Car_top
PLAYER_WIDTH = OBJ_DICT['player'][0]    # size_x = 20
PLAYER_HEIGHT = OBJ_DICT['player'][1]   # size_y = 30

# 경찰차 -- 경광등 때문에 폭이 더 넓다.
ENEMY_WIDTH = OBJ_DICT['enemy'][0]    # size_x = 25
ENEMY_HEIGHT = OBJ_DICT['enemy'][1]   # size_y = 30


if __name__ == '__main__':
    print(DESTIN_DIR)
