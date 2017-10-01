class Aircraft(object):
    def __init__(self, max_ammo, base_damage):
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
        pass

    def get_status(self):
        pass

        



f_16 = Aircraft(8, 30)
f_35 = Aircraft(12, 50)

print(f_16.refill(50))
print(f_16.ammo_store)