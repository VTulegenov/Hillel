
s = input('введите текст:')

s = s.split()
wort1, wort2 = s
print(wort1)
print(wort2)

s_file = open('home.txt', 'w')

print('Cлово 1: {0}; Cлово 2: {1};'.format(wort1[::-1], wort2[::-1]), file=s_file, end=' ', sep='"""')

print(f'Cлово 1: {wort1.upper()}; Cлово 2: {wort2.capitalize()}; ', file=s_file, end=' ', sep='"""')

print('!Cлово 1: %s; Cлово 2: %s;?' % (wort1, wort2), file=s_file, end=' ', sep='"""')

s_file.close()





