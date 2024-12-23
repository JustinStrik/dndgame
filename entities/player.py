from entities.entity import Entity

class Player(Entity):
    hp = 20
    name = "DefaultPlayer"
    holding = None

    def __init__(self, name, hp):
        super().__init__(name, hp)
        self.hp = hp
        self.name = name

    # init with weapon
    def __init__(self, name, hp, weapon):
        super().__init__(name, hp)
        self.hp = hp
        self.name = name
        self.holding = weapon

    def take_turn(self):
        # Implement the player's turn logic here
        print(f"{self.name} is taking their turn.")
        # Example: Player attacks an enemy
        self.attack()
        self.turn_complete = True

    def attack(self):
        # Placeholder for attack logic
        print(f"{self.name} attacks noone")

    # attack a specific entity
    def attack(self, entity):
        weapon = self.holding
        damage = weapon.damage
        entity.hp -= damage
        print(f"{self.name} attacks {entity.name} for {damage} damage!")

    def cast_spell(self, spell):
        # Placeholder for spell casting logic
        if self.mana >= spell.mana_cost:
            self.mana -= spell.mana_cost
            print(f"{self.name} casts {spell.name}!")
        else:
            print(f"{self.name} does not have enough mana to cast {spell.name}.")

# Example usage
if __name__ == "__main__":
    player = Player("Player", 100, 10)
    player.take_turn()
    player.cast_spell(Spell("Fireball", 20))  # Assuming a Spell class exists
