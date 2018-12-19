class Car:
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color
        self.speed = 0

    def accelerate(self, how_much):
        self.speed += how_much

    def decelerate(self):
        self.speed -= 10

    def change_speed(self, how_much):
        self.speed += how_much


class Garage:
    def __init__(self, size, color, car):
        self.size = size
        self.color = color
        self.car = car

    def drive_car_out(self):
        self.car = None
        return car

    def drive_car_in(self, car):
        self.car = car


car = Car('Honda', 'Civic', 'Blue')
print('the car is going:')
print(car.speed)
print('the car accelerates')
car.change_speed('a whole lot')
print('the car is going:')
print(car.speed)
print('the car slows down')
car.decelerate()
print('the car is going:')
print(car.speed)