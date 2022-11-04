from pico2d import *
#import move_player
import stats_data
from random import randint

open_canvas()

mob = load_image('slime_sheet_fix.png')

x = randint(100,700)
y = randint(100, 500)

def x_dot_y ():
    global x, y

    x = randint(100, 700+1)
    y = randint(100, 500 + 1)
# =========================================
def move_slime(x, y):
    frame = 0
    bottom = 0
    try_num = 0

    while (stats_data.rabbit[0] == 50):
        clear_canvas()
        mob.clip_draw(frame * 100, bottom, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 15
        if try_num  < 5:
            x += 10
            try_num += 1
            delay(0.03)
        elif try_num <10:
            y += 10
            try_num += 1
        elif try_num < 15:
            x -= 10
            try_num += 1
            delay(0.03)
        elif try_num <20:
            y -= 10
            try_num += 1
        elif try_num == 20:
            try_num = 0

        print(try_num)

        delay (0.1)
        get_events()
# =========================================

move_slime(x, y)

close_canvas()