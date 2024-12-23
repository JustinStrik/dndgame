# Club	1 sp	1d4 bludgeoning	2 lb.	Light
from items.weapons.melee.melee_weapon import MeleeWeapon
from utils.damage import DamageType, roll_damage

class Club(MeleeWeapon):

    def __init__(self):
        super().__init__(name="Club", damage=[4], bonus=0, constant_damage=0)
        self.value = 1
        self.weight = 2
        self.properties = ["Light"]
        self.light = True
        self.name = "Club"
        self.damage = [4]
        # self.bonus = 0 # not needed, because default set in super()
        # self.constant_damage = 0
        self.reach = 4
        self.damage_type = DamageType.BLUDGEONING
        

