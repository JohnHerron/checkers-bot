class Pawn:
    def __init__(self, location, color) -> None:
        self.king = False
        self.location = location
        self.color = color
        self.moves = self.generate_moves()

    def move_to(self, new_location):
        self.location = new_location
