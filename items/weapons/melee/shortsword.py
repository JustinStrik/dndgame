# extend weapon class to create a shortsword class
from weapons.weapon import Weapon

class Shortsword(Weapon):
    def __init__(self):
        super().__init__("Shortsword", [6], 0, 0)
        self.name = "Shortsword"
        self.damage = [6]
        self.bonus = 0
        self.constant_damage = 0
        