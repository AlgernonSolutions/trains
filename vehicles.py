class Vehicle(object):
    def __init__(self, curb_weight):
        self._curb_weight = curb_weight

    @property
    def curb_weight(self):
        return self._curb_weight


class Sedan(Vehicle):
    def __init__(self, number_doors, number_wheels):
        self._number_doors = number_doors
        super.__init__(number_wheels)


class PickupTruck(Vehicle):
    def __init__(self, bed_size, number_wheels):
        self._bed_size = bed_size
        super().__init__(number_wheels)


class ElCamino(Sedan, PickupTruck):
    def __init__(self, color, number_doors, bed_size, number_wheels):
        super().__init__(number_doors, number_wheels)
        kwargs = {
            'bed_size': bed_size,
            'number_doors': number_doors,
            'number_wheels': number_wheels
        }
        # PickupTruck.__init__(self, bed_size=bed_size, number_wheels=number_wheels)
        self._color = color


jeffs_camino = ElCamino('black', 2, 300, 4)
print()
