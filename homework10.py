array = [1, 1, 3, 5, 8, 7, 9, 8, 9, 7, 1, 9, 4, 8, 2, 3, 5, 6, 3, 4, 0, 5, 8, 9, 1]

array_d = {}.fromkeys(array, 0)
for a in array:
    array_d[a] += 1

print(array_d)

