#3 Напишіть класс Parallelogram, який приймає два аргументи width і length і метод
# get_area, який вираховує площу паралелограма. Успадкуйте від нього клас Square, перевизначіть в ньому метод
# get_area таким чином, щоб він вираховував площу квадрату.

class Parallelogram:
    def __init__(self, width, length=0):
        self.a = width
        self.h = length

    def get_area(self):
        print(self.a * self.h)

p = Parallelogram(6, 4)
p.get_area()

class Square(Parallelogram):
    def get_area(self):
        print(self.a ** 2)

s = Square(6)
s.get_area()