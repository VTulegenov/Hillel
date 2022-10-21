import random


def blok_1():
    while True:
        answer = int(input('введите свои предположения какое это число:'))
        if answer == value:
            print('=' * 60)
            print('Вы угадали!')
            print('=' * 60)
            exit()
        elif answer < value:
            print('Число больше загаданного!')
        elif answer > value:
            print("Число меньше загаданного!")


print('Добро пожаловать в угодайку!')
rule = input('Хотите прочитать правила? ДА/НЕТ: ')

if rule.upper() in 'ДА':
    print('-' * 60)
    print('Правила таковы что вам нужно выбрать уровень от 1-3 ')
    print('1 - сложность легкая, нужно угадать число в приделе от 1-10')
    print('2 - сложность средняя, нужно угадать число в приделе от 1-20')
    print('3 - сложность тяжелая, нужно угадать число в приделе от 1-30')
    print('-' * 60)
    lvl1 = input('выберите сложность:')
#блок1
    while True:
        if int(lvl1) != 3 and int(lvl1) != 2 and int(lvl1) != 1:
            lvl1 = input('Ошибка повторите ввод:')
            continue
        elif int(lvl1) == 1:
            value = random.randint(1, 10)

            print('Число сгенирировано!')
            blok_1()
        elif int(lvl1) == 2:
            value = random.randint(1, 20)

            print('Число сгенирировано!')
            blok_1()
        elif int(lvl1) == 3:
            value = random.randint(1, 30)

            print('Число сгенирировано!')
            blok_1()

#блок2
elif rule.upper() in 'НЕТ':
    lvl1 = input('выберите сложность:')
    while True:
        if int(lvl1) != 3 and int(lvl1) != 2 and int(lvl1) != 1:
            lvl1 = input('Ошибка повторите ввод:')
            continue
        elif int(lvl1) == 1:
            value = random.randint(1, 10)

            print('Число сгенирировано!')
            blok_1()
        elif int(lvl1) == 2:
            value = random.randint(1, 20)

            print('Число сгенирировано!')
            blok_1()
        elif int(lvl1) == 3:
            value = random.randint(1, 30)

            print('Число сгенирировано!')
            blok_1()


