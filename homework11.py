

inputdata = ('Страна', 'шалаш', 'Летел', 'вертолёт', 'УЧУ', 'мэм', 'язык')
result = filter(lambda x: x.lower() == x.lower()[::-1], inputdata)
print(tuple(result))

