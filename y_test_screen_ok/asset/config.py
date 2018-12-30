"""-------------------------
# 01.Config.py - 의존성이 없는 독립 모듈을 만들어보자
#
#
#\n\n\n"""
print(__doc__)


FPS = 20

""" # COLOR TABLE """
BLACK = (0, 0, 0)           # #000000
WHITE = (255, 255, 255)     # #ffffff
RED = (255, 0, 0)           # #ff0000
GREEN = (0, 255, 0)         # #00ff00
BLUE = (0, 0, 255)          # #0000ff
DARKGRAY = (50, 50, 50)     # #505050


"""# 스크린 환경설정 변수"""
SCREEN_TITLE = 'HEY.........TEST!!!'
(PAD_WIDTH, PAD_HEIGHT) = SCREEN_SIZE = (360, 480)
FONT_COLOR = BLACK


"""# 오브젝트 정보저장"""
# OBJ_KEY(NAME) : [
#   DIR_from_ROOT.
#   FIRST_IMG
#   ANIM = (True, Num_sprites)
#   SIZE = (height, width)

OBJ_DICT = {
    'police': [
        './asset/img/',
        'kr_police_0.png',
        (True, 8),
        (32, 28),
    ],

    'player': [
        './asset/img/',
        'car_top.png',
        (False, 1),
        (32, 22),
    ],
}


if __name__ == '__main__':
    print(POSXY)
    POSX = 120
    POSY = 50
    print(POSX)
    print(POSY)
    print(POSXY)
    pass
