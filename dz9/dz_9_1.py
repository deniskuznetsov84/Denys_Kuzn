#1 Напишіть клас автомобіля з атрибутами: марка, колір, об'єм двигуна.
# Та методами: їхати вперед, їхати назад. Напишіть ще один клас автомобіля, який є успадкованим
# від першого. Додайте в нього методи повороту праворуч та ліворуч

class Car1:
    def __init__(self, brand, color, engine_capacity):
        self.brand = brand
        self.color = color
        self.engine_capacity = engine_capacity

    def drive_forward(self):
        print('Drive forward')

    def drive_back(self):
        print('Drive back')

class Car2(Car1):
    def turn_right(self):
        print('Turn right')

    def turn_left(self):
        print('Turn left')

my_car = Car2('Renault', 'white', 2.0)
print(my_car.brand)
print(my_car.color)
print(my_car.engine_capacity)
my_car.drive_forward()
my_car.drive_back()
my_car.turn_left()
my_car.turn_right()