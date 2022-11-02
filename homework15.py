b = b'r\xc3\xa9sum\xc3\xa9'
a = b.decode()
print(a)
v = a.encode('Latin1')
print(v)
d = v.decode('Latin1')
print(d)
