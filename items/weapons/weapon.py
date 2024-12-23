from enum import Enum
from items.item import Item
from utils.damage import DamageType
from utils.damage import roll_damage as util_roll_damage # change name to avoid conflict with roll_damage in utils/damage.py

class Weapon(Item):
    name = "DefaultWeapon"
    ammunition = 0
    finesse = False
    heavy = False
    light = False
    loading = False
    range = 0
    reach = False
    special = False
    thrown = False
    two_handed = False
    versatile = False
    improvised = False
    silvered = False
    simple = False
    martial = False
    damage = []
    damage_type = DamageType.BLUDGEONING

    def __init__(self, name, damage, bonus, constant_damage):
        self.name = name
        self.damage = damage
        self.bonus = bonus
        self.constant_damage = constant_damage


    def __str__(self):
        return f"{self.name}: {self.damage} + {self.bonus} + {self.constant_damage}"
    
    def roll_damage(self, modifier):
        return util_roll_damage(self, modifier)
    
    def roll_damage(self):
        return util_roll_damage(self, 0)