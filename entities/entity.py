class Entity():
    x = 0
    y = 0
    is_turn_complete = False

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_turn_complete(self, is_turn_complete):
        self.is_turn_complete = is_turn_complete

    def get_turn_complete(self):
        return self.is_turn_complete
    
    def is_turn_complete(self):
        return self.is_turn_complete