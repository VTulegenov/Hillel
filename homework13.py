
values = [10, 100.2,  2, '3', 'forth', 'end', 99, True, None, 10.1, 100]

result = map(lambda x: str(x) if x != True and isinstance(x, int) else x, values)

print(list(result))

