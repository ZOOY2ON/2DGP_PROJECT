from random import randint
import stats_data

rabbitfoot = 0
rabbitborn = 0
slimex = 0
true = 0
my_item = [0, 0, 0, 0] # 토끼발, 토끼뼈, 슬라임 핵의 조각, 포션(미정)

random_num_rabbitfoot = 0
random_num_rabbitborn = 0
random_num_slimex = 0
# 아이템 : 토끼발 10개 / 뼈 3개 // 슬라임 핵의 조각 30개
# ---- 토끼 25마리 정도 잡으면 나올듯
# 토끼발 : 50퍼
# 토끼뼈 확률 : 20퍼
# ---- 슬라임 40~50마리 정도 잡으면 나올듯
# 슬라임 핵의 조각 : 75퍼

while true < 60:
    stats_data.rabbit[0] = 0
    stats_data.slime[0] = 0

    if stats_data.rabbit[0] == 0:
        random_num_rabbitfoot = randint(0, 2)
        random_num_rabbitborn = randint(0, 5)
        if random_num_rabbitfoot == 0:
            rabbitfoot += 1
        if random_num_rabbitborn == 0:
            rabbitborn += 1

    if stats_data.slime[0] == 0:
        random_num_slimex = randint(0, 4)
        if random_num_slimex == 0:
            slimex += 1
        elif random_num_slimex == 1:
            slimex += 1
        elif random_num_slimex == 2:
            slimex += 1

    my_item[0] = rabbitfoot
    my_item[1] = rabbitborn
    my_item[2] = slimex

    print('---------------------------------------------')
    print(random_num_rabbitfoot)
    print(random_num_rabbitborn)
    print(random_num_slimex)
    print('---------------------------------------------')
    print('========================')
    print('토끼발 : ' , my_item[0])
    print('토끼뼈 : ' , my_item[1])
    print('슬라임 핵의 조각 : ' , my_item[2])
    print('========================')

    true += 1
