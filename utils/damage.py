from enum import Enum
import random

class DamageType(Enum):
    BLUDGEONING = 1
    PIERCING = 2
    SLASHING = 3

# roll damage with modifier
def roll_damage(weapon, modifier):
    # weapon damage dice stored as array of dice values
    # e.g. [6, 6] represents 2d6
    damage = sum([random.randint(1, die) for die in weapon.damage]) + weapon.bonus + weapon.constant_damage
    return damage + modifier

# roll damage no modifier
def roll_damage(weapon):
    return roll_damage(weapon, 0)