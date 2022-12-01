
class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_coord(self):
        return self.x, self.y

    @staticmethod
    def norm2(x, y):
        return x*x + y*y


m = MyClass(1, 2)
res = m.get_coord()
print(res)

print(m.norm2(5, 6))
