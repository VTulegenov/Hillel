

while True:
    print('если хотите выйти введите:ВЫХОД, EXIT, QUIT, E, Q')
    value = input('Ведите число:')

    if value.upper() in ("ВЫХОД", "EXIT", "QUIT", "E", "Q"):
        break

    elif value.isdigit():
        print('Вы ввели число: ' + value)

    elif '-' in value and not '.' in value and value.isdigit():
        print('Вы ввели отрицательное число: ' + value)

    elif '-.' in value and value.isdigit():
        print('Вы ввели отрицательное дробное число: ' + value[:1], '0', value[1:], sep='')

    elif '-' in value and '.' in value and value.isdigit():
        print('Вы ввели отрицательное дробное число: ' + value)

    elif '.' in value and value.isdigit():
        print('Вы ввели дробное число: ' + value)

    else:
        print("Вы ввели не корректное число: " + value)








