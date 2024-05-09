
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

    def move_bot(self):
        print("bot turn")
        pawn, move = self.algorithm(self.game, 1, self.game.state)[1]
        print(f"pawn is: {pawn}, move is: {move}")
        self.game.move_pawn(self.game.board.get_square(pawn[1], pawn[0]).get_pawn(), self.game.board.get_square(move[1],move[0]), player = False)
        self.game.switch_turn()
