from pico2d import *

# =========================== 변수 S
running = True
stage = 1
x = 800 // 2 ;   y = 90
frame = 0
bottom = 0
dir_x = 0 ;  dir_y = 0
way = 0     #이전 방향
attack = 0  # 공격 ( 물리 : 1 / 마법 : 2 )
# =========================== 변수 E

# =========================== 키보드 입력 S
def handle_events():
    global running
    global dir_x ; global dir_y
    global attack
    global stage

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        # 키보드가 눌러짐
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir_x += 1
            elif event.key == SDLK_LEFT:
                dir_x -= 1
            elif event.key == SDLK_UP:
                dir_y += 1
            elif event.key == SDLK_DOWN:
                dir_y -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
            # 공격키
            if event.key == SDLK_q:
                attack = 1
            elif event.key == SDLK_w:
                attack = 2

        # 키보드가 올라옴
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir_x -= 1
            elif event.key == SDLK_LEFT:
                dir_x += 1
            elif event.key == SDLK_UP:
                dir_y -= 1
            elif event.key == SDLK_DOWN:
                dir_y += 1
# =========================== 키보드 입력 E

# =========================== 움직임 출력 S
def draw_move(bottom, cut):
    global frame
    global x, y, dir_x, dir_y
    global  way
    global stage

    clear_canvas()
    background.draw(400, 300)

    # === 정지 모션
    if bottom == 800:
        if way == 1:
            frame = 2
        elif way == 2:
            frame = 3
        elif way == 3:
            frame = 1
        elif way == 4:
            frame = 0
        # === 정지 모션
    draw_attack()

    character.clip_draw(frame * 100, bottom * 1, 100, 100, x, y)
    # 스테이지 3 맨 앞 오브젝트
    if stage == 3:
        tree.draw(400, 300)
    update_canvas()

    handle_events()
    if bottom != 800:
        frame = (frame + 1) % cut

    print(bottom)
    print(way)
    if x >= 50 and x <= 750:
        x += dir_x*16

    if x <50:
        dir_x = 0
        x = 55
    if x>750:
        dir_x = 0
        x = 745

    if y >= 50 and y<=550:
        y += dir_y*16

    if y < 50:
        dir_y = 0
        y = 60
    if y>550:
        dir_y = 0
        y = 540



    delay(0.1)
# =========================== 움직임 출력 E

# =========================== 공격 움직임 출력 S
def draw_attack():
    global frame ; global bottom ; global cut
    global x, y, dir_x, dir_y
    global  way
    global attack

    clear_canvas()
    background.draw(400, 300)
    cut = 4

    # === 공격 방향
    if attack == 1:
        bottom = (way+3)*100

    elif attack == 2:
        bottom = (way-1)*100

    elif attack == 0:
        return
        # === 공격 방향

    character.clip_draw(frame * 100, bottom * 1, 100, 100, x, y)
    update_canvas()

    handle_events()

    frame = (frame + 1) % 4

    x += dir_x * 16
    y += dir_y* 16

    delay(0.1)
    draw_move(800, 1)
    print(way)
# =========================== 공격 움직임 출력 E

# =========================== 이미지 로딩 S
open_canvas()
if stage == 1:
    background = load_image('stage_1.png')
elif stage == 2:
    background = load_image('stage_2.png')
elif stage == 3:
    background = load_image('stage_3.png')
    tree = load_image('stage_3_tree.png')
elif stage == 4:
    background = load_image('stage_4.png')
character = load_image('player_all_sheet_02.png')
# =========================== 이미지 로딩 E

# =========================== main S
while running:
    if dir_x == 1:
        draw_move(900,2)
        way = 1 #오른쪽
    elif dir_x == -1:
        draw_move(1000,2)
        way = 2 # 왼쪽
    elif dir_y == 1:
        draw_move(1100,2)
        way = 3 # 위
    elif dir_y == -1:
        draw_move(1200,2)
        way = 4 # 아래
    elif dir_x == 0 or dir_y == 0:
        draw_move(800,1)
   # if attack == 1:
        #draw_move(400, 4)
    #if attack == 2:
        #draw_move((way-1)*100, 4)
    draw_attack()

close_canvas()
# =========================== main E