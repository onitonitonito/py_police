"""
# Main.py - 함수 들 모음 (2번째 모듈에서 문제가..)
#
#\n\n\n"""
print(__doc__)

from config import *         # 따로 저장한 변수를 불러온다.



"""  CALCULATE """
def draw_socre(count):
    global DISPLAYSURF
    font = pygame.font.Font("freesansbold.ttf", 20)
    text = font.render("Arrest Crime: "+ str(count), True, FONT_COLOR)
    DISPLAYSURF.blit(text, (5, 10))


if __name__ == '__main__':
    pass
