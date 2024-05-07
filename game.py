
class Game:
    def __init__(self, game, algorithm) -> None:
        self.game = game
        self.algorithm = algorithm
    
    def getWinner(self):
        return self.game.winner
    
    def handle_click(self, square):
        if self.game.turn == 'GREEN':
            return
        self.game.handle_click(square)
        if self.game.turn == 'GREEN':
            self.move_bot()

    def move_bot(self):
            # TODO: implement minimax turn selection
            self.game.switch_turn()
