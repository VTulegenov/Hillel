class String(str):

    def __add__(self, other):
        return String(f'{self}{str(other)}')

    def __sub__(self, other):
        result = self.split(str(other), 1)
        return String(''.join(result))
