

class auto:
    brand = True
    age = 1
    cоlor = True
    mark = True
    weight = True

    def __init__(self, brand, age, mark):
        self.brand = brand
        self.age = age
        self.mark = mark

    def move(self):
        print('move')
    def birthday(self, age):
        self.age = age
        age += 1
        print(age)
    def stop(self):
        print('stop')

auto_1 = auto('brand', 'age', 'mark')
auto_1.move()
auto_1.birthday(1)
auto_1.stop()
auto_1.birthday(1)
auto_1.birthday(1)
