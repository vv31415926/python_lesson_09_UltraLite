'''
1. Создать свои классы
2. Добавить методы в классы
3. Использовать инкапсуляцию, наследование, полиморфизм
'''
class Animal():
    def __init__(self, length, height, weight, color):
        self._length = length
        self._height = height
        self._weight = weight
        self._color = color

    def get_length(self):
        return self._length
    def get_height(self):
        return self._height
    def get_weight(self):
        return self._weight
    def get_color(self):
        return self._color

class Cat( Animal ):
    def __init__(self, length, height, weight, color ):
        super().__init__( length, height, weight, color)
        self._voice = 'мяу-мяу'

    def get_voice(self):
        return self._voice


class Dog(Cat):
    def __init__(self, length, height, weight, color):
        super().__init__( length, height, weight, color)
        self._voice = 'гав-гав'


if __name__ == '__main__':
    cat = Cat( 30,20,2,'серополосатый')
    dog = Dog( 50,40,4,'черный')

    print( cat.get_voice(), cat.get_color() )
    print( dog.get_voice(), dog.get_color() )
