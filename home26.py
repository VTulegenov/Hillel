def ar_progresion(a_n, d, k):
    i = 0
    for i in range(k):
        q = a_n * d
        print(q)
        a_n = q

Y = int(input('Введите первый эл-нт прогрессии: '))
r = int(input('Введите разность прогрессии: '))
kol = int(input('Введите кол-во эл-ов прогрессии: '))
ar_progresion(Y, r, kol)
