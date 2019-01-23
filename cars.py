class Car:
    def __init__(self, make=None, model=None, color=None, **kwargs):
        if speed is None:
            speed = []
        has_four_wheel_drive = kwargs['four_wheel_drive']
        self._make = make
        self._model = model
        self._color = color
        self._speed = speed

    @property
    def is_moving(self):
        if self.speed > 0:
            return True
        return False

    @property
    def speed(self):
        return self._speed

    @property
    def make(self):
        return self._make

    @property
    def model(self):
        return self._model

    @property
    def color(self):
        return self._color

    def accelerate(self, how_much):
        self._speed += how_much

    def decelerate(self):
        self._speed -= 10

    def change_speed(self, how_much, direction='forward'):
        how_much = abs(how_much)
        if direction == 'backwards':
            how_much = -1 * how_much
        self._speed += how_much


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


class Table:
    def __init__(self, table_name, **kwargs):
        rows = []
        for table_row in kwargs['table_rows']:
            created_row = TableRow(**table_row)
            rows.append(created_row)
            print(created_row.__dict__)
        self._rows = rows
        self._table_name = table_name


class TableRow:
    def __init__(self, row_id, name, **kwargs):
        self._row_id = row_id
        self._name = name
        self._others = kwargs

    def get_cell(self, cell_name):
        if cell_name == 'row_id':
            return self._row_id
        if cell_name == 'name':
            return self._name
        if cell_name in self._others:
            return self._others[cell_name]
        raise AttributeError('cell name not found')


car_kwargs = {
    'make': 'Honda',
    'model': 'Civic',
    'color': 'Blue',
    'speed': 0,
    'four_wheel_drive': False
}

table_data = {
    'table_name': 'inventory',
    'table_rows': [
        {'row_id': 1, 'name': 'Cod', 'boat_name': 'The Ocean Queen'},
        {'row_id': 1, 'name': 'door hinge', 'bin_number': 4}
    ]
}
table = Table(**table_data)

car = Car(**car_kwargs)
print('the car is going:')
print(car.speed)
print('the car accelerates')
# car.accelerate(10)
car.change_speed(how_much=10, direction='backward', nice_day=True)
print('the car is going:')
print(car.speed)
print('the car slows down')
car.decelerate()
print('the car is going:')
print(car.speed)