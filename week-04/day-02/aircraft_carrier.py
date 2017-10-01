class Aircraft(object):
    def __init__(self, aircraft_type, max_ammo, base_damage):
        self.aircraft_type = aircraft_type
        self.max_ammo = max_ammo
        self.base_damage = base_damage
        self.ammo_store = 0
        if self.ammo_store > self.max_ammo:
            self.ammo_store = self.max_ammo
        else:
            pass

    def fight(self):
        self.damage = self.ammo_store * self.base_damage
        self.ammo_store = 0
        return self.damage

    def refill(self, amount):
        if amount >= self.max_ammo:
            self.ammo_store = self.max_ammo
            return amount - self.max_ammo
        else:
            self.ammo_store += amount
        return 0
           
    def get_type(self):
        return self.aircraft_type

    def get_status(self):
        return ("Type: {}, Ammo: {}, Base Damage: {}, All Damage: {}.".format(self.aircraft_type, self.ammo_store, self.base_damage, self.base_damage*self.ammo_store))

        



f_16 = Aircraft("F-16", 8, 30)
f_35 = Aircraft("F-35", 12, 50)

print(f_16.get_type())
print(f_16.get_status())

f_16.refill(30)
print(f_16.get_type())
print(f_16.get_status())
