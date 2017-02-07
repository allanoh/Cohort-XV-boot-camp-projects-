class Car(object):
    name = None
    model = None
    num_of_doors = None
    num_of_wheels = None
    car_type = None
    speed = 0
    is_type_saloon = None

    def __init__(self, car_name="General", car_model="GM", vehicle_type="saloon", speed=0):
        self.name = car_name
        self.model = car_model
        self.car_type = vehicle_type
        self.speed = speed

        if self.name == "Porshe" or self.name == "Koenigsegg":
            self.num_of_doors = 2
        else:
            self.num_of_doors = 4

        if self.car_type == "trailer":
            self.num_of_wheels = 8
            self.is_type_saloon = False
        else:
            self.num_of_wheels = 4
            self.is_type_saloon = True

    def is_saloon(self):
        return self.is_type_saloon

    def drive(self, mov_speed=80):
        if self.car_type == "trailer":
            self.speed = 77
        elif self.name == "Mercedes":
            self.speed = 1000
        else:
            self.speed = mov_speed

        return self

