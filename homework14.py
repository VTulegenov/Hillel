

while True:
    value = input('Ведите число:')

    if value.upper() in ("ВЫХОД", "EXIT", "QUIT", "E", "Q"):
        break

    elif value.isdigit():
        print('Вы ввели число: ' + value)

    elif '-' in value and not '.' in value:
        print('Вы ввели отрицательное число: ' + value)

    elif '-.' in value:
        print('Вы ввели отрицательное дробное число: ' + value[:1], '0', value[1:], sep='')

    elif '-' in value and '.' in value:
        print('Вы ввели отрицательное дробное число: ' + value)

    elif '.' in value:
        print('Вы ввели дробное число: ' + value)

    elif not value.isdigit():
        print("Вы ввели не корректное число: " + value)








