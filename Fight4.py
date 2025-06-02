import time
import os
from random import randint
# stroke_to_typewrite = "Hello, this is a typewriter effect example"
# Появление
# for letter in stroke_to_typewrite:
#     print(letter, end='', flush=True)
#     time.sleep(0.1)
#
# for i in range(len(stroke_to_typewrite) + 1, -1, -1):
#     print('\r' + stroke_to_typewrite[:i], end=' ', flush=False)
#     time.sleep(0.1)
#
# print('This is what will be displayed after')
day = 0
sleep = 0
flashlight = 0
count_meet = 0
invent = {'stone': 0, 'gold': 0, 'dimond': 0}
charecter = {'lucky': 20, 'money': 0, 'stamina':10, 'lvl_pickaxe': 1, 'def_stamina':10}
price = {'stone': 5, 'gold': 10, 'dimond': 20,}
apartment = 2000000

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def text_a(x):
    for i in x:
        print(i, end='', flush=True)
        time.sleep(0.03)


def text_b(x):
    for i in x:
        print(i, end='', flush=True)
        time.sleep(0.01)


def text_sl(x):   
    for i in x:
        print(i, end='', flush=True)
        time.sleep(0.5)


def check(a):
    if a == 'info':
        print(charecter)
    elif a == 'invent':
        print(invent)

def sell_stone():
    global invent, price
    text_a('сколько ты хочешь продать?')
    print(invent['stone'])
    how_mach = 0
    how_mach = int(input('how_mach\n'))
    check(how_mach)
    if how_mach > int(invent['stone']):
        text_a('у тебя нету столько')
    elif how_mach <= int(invent['stone']):
        text_a(f'я тебе дам за {how_mach} камней +{invent['stone'] * price['stone']} монет')
        charecter['money'] = how_mach * price['stone']
        invent['stone'] -= how_mach


def mine():
    global invent, charecter
    from random import randint
    lucky = randint(1, charecter['lucky'])

    if lucky == 1 and charecter['lvl_pickaxe'] == 3:
        cls()
        invent['dimond'] += 1
        text_a('+1 dimond')
    elif lucky < 5 and charecter['lvl_pickaxe'] == 2:
        cls()
        invent['gold'] += 1
        text_a('+1 gold')
    elif lucky < 10 and charecter['lvl_pickaxe'] == 1:
        cls()
        invent['stone'] += 1
        text_a('+1 stone')
    else:
        cls()
        text_a('nothing')


def cave():
    while charecter['stamina'] != 0:
        cls()
        text_in_cove = 'вы в шахте, чтобы ударить киркой напишите "a"\n'
        text_a(text_in_cove)
        for i in range(charecter['stamina']):
            charecter['stamina'] -= 1
            home_or_main = input('\n')
            if home_or_main == 'a':
                mine()
            elif home_or_main == 'exit':
                break
            elif home_or_main == 'info' and flashlight != 0:
                cls()
                print(charecter)
            elif home_or_main == 'info' or home_or_main == 'invent' and flashlight == 0:
                cls()
                text_sl('Тут темно')
            else:
                cls()
                text_a('если вы хотите выйти "exit"')
    cls()


def sell():
    door = 0
    global count_meet
    count_meet += 1
    cls()
    visiting = 0
    while door == 0:
        visiting += 1

        if count_meet == 1 and visiting == 1:
            text_a('привет я покупаю камни\nну и перепродаю алмазы и золото но в основном камни\nУ ТЕБЯ ЕСТЬ КАМНИ ?!')
        elif count_meet != 1 and visiting == 1:
            text_a('привет что у тебя на этот раз')
        sell_res = 0
        sell_res = input('sell_res\n')
        check(sell_res)
        if sell_res == 'stone':
            sell_stone()
            # how_mach = input()
            # if charecter['stone'] < how_mach:
            #     text_a('у тебя нету столько')
            # elif charecter['stone'] >= how_mach:
            #     text_a('Ураа\n')
            #     text_b(f'Я буре вот твои деньги {price['stone'] * how_mach} за {how_mach} камней')
            #     charecter['money'] = price['stone'] * how_mach
            #     invent['stone'] -= how_mach
        if sell_res == 'gold':
            how_mach = input()
            if charecter['gold'] < how_mach:
                text_a('у тебя нету столько')
            elif charecter['gold'] >= how_mach:
                text_a('Ураа\n')
                text_b(f'Я буре вот твои деньги {price['gold'] * how_mach} за {how_mach} камней')
                charecter['money'] = price['stone'] * how_mach
                invent['gold'] -= how_mach
        else:
            text_b('Если ты хочешь продать "stone" "gold" "dimond"')
cls()
start_text = 'вы шахтёр ваша задача накопить на квартиру в Бишкеке\n'
text_a(start_text)
while 1:
    sleep = 0
    if day != 0:
        cls()
        text_b('Доброе утро пора в шахту\n')
    day += 1
    while sleep == 0:
        if charecter['stamina'] == 0:
            text_a('вы устали ваша стамина 0\n')
        if day != 0 and charecter['stamina'] == 0:
            text_b('\nвы можете поспать дома "home"\nчтобы посмотреть инвентарь "invent"\nузнать свои характеристики "info"\nпродать ресурсы "sell"\n')
        text_b('чтобы зайти в шахту напишите "start"\n')
        main_menu = 0
        main_menu = input('')
        check(main_menu)
        if main_menu == 'start':
            cave()
        elif main_menu == 'home':
            cls()
            text_b('вы дома у мамы и спите\n')
            time.sleep(0.5)
            text_sl('ZzZzZzZ\n')
            charecter['stamina'] = charecter['def_stamina']
            sleep = 1
        elif main_menu == 'sell':
            sell()
print('lol')