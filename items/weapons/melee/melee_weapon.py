from weapons.weapon import Weapon
# import weapons.weapon

class MeleeWeapon(Weapon):
    reach: int = 4
    
    def __init__(self, name, damage, bonus, constant_damage):
        super().__init__(name, damage, bonus, constant_damage)
        self.name = name
        self.damage = damage
        self.bonus = bonus
        self.constant_damage = constant_damage

    def __str__(self):
        return f"{self.name}: {self.damage} + {self.bonus} + {self.constant_damage}"
    
    # reach
