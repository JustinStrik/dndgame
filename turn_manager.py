class TurnManager:
    def __init__(self):
        self.entities = []
        self.current_turn = 0

    def add_entity(self, entity):
        self.entities.append(entity)

    def next_turn(self):
        self.current_turn = (self.current_turn + 1) % len(self.entities)
        current_entity = self.entities[self.current_turn]
        current_entity.take_turn()

    def update(self):
        # Call this method in your game loop to handle turns
        current_entity = self.entities[self.current_turn]
        if current_entity.is_turn_complete():
            self.next_turn()

class Entity:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power
        self.turn_complete = False

    def take_turn(self):
        # Placeholder for entity's turn logic
        print(f"{self.name} is taking their turn.")
        self.turn_complete = True

    def is_turn_complete(self):
        return self.turn_complete

    def reset_turn(self):
        self.turn_complete = False

# Example usage
if __name__ == "__main__":
    turn_manager = TurnManager()
    player = Entity("Player", 100, 10)
    enemy = Entity("Enemy", 100, 10)

    turn_manager.add_entity(player)
    turn_manager.add_entity(enemy)

    for _ in range(5):  # Simulate 5 turns
        turn_manager.update()
