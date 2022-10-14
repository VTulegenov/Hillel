


print('Добрый день!')
print(('Как вас зовут?'))

name = input()

age = input('Укажите свой возраст:')

while True:
    age = input('Ошибка, повторите ввод:')

    if not age.isdigit() or int(age) <=0:
        continue
    elif int(age) < 10:
        print('Привет, шкет ' + name)
    elif int(age) < 18 >= 10:
        print('Как жизнь ' + name + '?')
    elif int(age)  > 18 < 100:
        print('Что желаете ' + name + '?')
    else:
        print(name + ' вы лжете - в наше время столько не живут...')
    answer = input('Хотите выйти? (Y/Д): ')
    if answer.upper() in ('Y','Д'):
            break