class Car:
    def __init__(self, make, model, color, year, max_speed=120):
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.max_speed = max_speed
        self._speed = 0

    @property
    def speed(self):
        mph_speed = self._speed * .621
        return mph_speed

    def accelerate(self):
        current_speed = self._speed
        new_speed = current_speed + 10
        self._speed = new_speed

    def brake(self):
        self._speed -= 10



jeffs_car = Car('Honda', 'Civic', 'Blue', 2001, 75)
print('jeffs car is going:')
print(jeffs_car.speed)
print('jeff accelerates the car')
jeffs_car.accelerate()
print('jeffs car is going')
print(jeffs_car.speed)
jeffs_car.speed += 10
print()
