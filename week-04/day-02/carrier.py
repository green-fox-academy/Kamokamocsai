from aircraft_carrier import Aircraft

class Carrier(object):
    def __init__(self, ammo, health):
        self.ammo_storage = ammo
        self.health = health
        self.aircrafts = []

    def add_aircraft(self, aircraft_type):
        f16_list = ["f-16", "f16", "F16", "F-16", "F 16", "f 16"]
        self.aircraft_type = aircraft_type
        if aircraft_type in f16_list:
            aircraft_type = Aircraft()
            self.aircrafts.append(aircraft_type)
            return self.aircrafts
        elif aircraft_type in f35_list:
            aircraft_type = Aircraft()
            self.aircraft_type.append(aircraft_type)
