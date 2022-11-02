
sting_1 = input('Введите первую строку: ')
sting_2 = input('Введите вторую строку: ')
sting_3 = input('Введите третью строку: ')
sting_4 = input('Введите четвертую строку: ')

s_file = open('homework.txt', 'w')
print(sting_1, file=s_file, end="\n", sep='')
print(sting_2, file=s_file, end='\n ', sep='')
s_file.close()

s_file = open('homework.txt', 'a')
print(sting_3, file=s_file, end="\n", sep='')
print(sting_4, file=s_file, end="\n", sep='')
s_file.close()


