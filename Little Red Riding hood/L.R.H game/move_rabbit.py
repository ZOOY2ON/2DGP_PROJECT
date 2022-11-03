from pico2d import *
#import move_player
import stats_data

open_canvas()

mob = load_image('rabbit_sheet.png')

x = 400
frame = 0
bottom = 0
try_x = 0

while (stats_data.rabbit[0] == 50):
    clear_canvas()
    mob.clip_draw(frame * 100, bottom, 100, 100, x, 90)
    update_canvas()
    frame = (frame + 1) % 6
    if try_x < 5:
        x += 10
        bottom = 0
        try_x += 1
        delay(0.03)
    if try_x >= 5:
        x -= 10
        bottom = 600
        try_x += 1
        delay(0.03)
    if try_x == 10:
        try_x = 0

    print(try_x)

    delay (0.08)
    get_events()

close_canvas()