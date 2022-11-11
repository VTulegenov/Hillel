
class Dog:
    number_of_foot = 4
    viviparous = True
    tail = True
    name = None

    def __int__(self, name, number_of_foot = 4, tail = True):
        self.name = name
        self.number_of_foot = number_of_foot
        self.tail = tail

    def say(self):
        print('Woof')

    def go(self):
        for item in range(1, self.number_of_foot + 1):
            print(f'step{item}')


Dog_1 = Dog('Bob',3)
dog_1.go()
dog_1.say()
print(Dog_1.number_of_foot)
dog_1.go()

Dog_2 = Dog()
Dog_2.go()
