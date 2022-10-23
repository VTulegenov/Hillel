dict_old = {1: 9, 2: 8, 3: 7, 4: 6, 5: 5, 6: 4, 7: 3, 8: 2, 9: 1}
print(dict_old)
dict_new = {v: k for k, v in dict_old.items()}
print(dict_new)