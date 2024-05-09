import random
from copy import deepcopy
import time

def minimax(game, depth, state, curr_pawn = None, curr_move = None):
    if depth == 0 or game.winner != None:
        if not curr_pawn or not curr_move:
            chosen_move = choose_random(game.calculate_all_moves(state), state)
            # if not chosen_move:
            #     return eval_func(state)
            curr_pawn = chosen_move[0]
            curr_move = chosen_move[1]
        return eval_func(state), (curr_pawn, curr_move)
    
    minEval = float('inf')
    best_play = None
    all_curr_moves = game.calculate_all_moves(state)
    curr_moves = deepcopy(all_curr_moves)
    # prune moves not playable by bot
    for pawn in all_curr_moves:
        pawn_y = int(pawn[:1])
        pawn_x = int(pawn[2:])
        if state[pawn_y][pawn_x] >= 0:
            del curr_moves[pawn]
    for pawn, moves in curr_moves.items():
        if depth == 3:
            game.toggle_select_pawn(game.board.get_square(int(pawn[2:]), int(pawn[:1])).get_pawn())
            # time.sleep(0.1)
            game.toggle_select_pawn(game.board.get_square(int(pawn[2:]), int(pawn[:1])).get_pawn())
        for move in moves:
            state = game.simulate_move(pawn, move, state)
            evaluation = minimax(game, depth-1, state, pawn, move)[0]
            minEval = min(minEval, evaluation)
            if minEval == evaluation:
                # tuple of pawn and move which are both tuples
                best_play = (int(pawn[:1]), int(pawn[2:])), move

    # randomly chooses move when there is no minimum
    if (not best_play):
        choose_random(curr_moves, state)
    return minEval, best_play

def eval_func(state):
    sum = 0
    for row in state:
        for pawn in row:
            sum += pawn
    print(sum)
    return sum

def choose_random(curr_moves, state):
    print("NO BEST PLAY:")
    moves_copy = deepcopy(curr_moves)
    print(curr_moves)

    # retry if there are no valid moves for the chosen pawn
    found = False
    while(not found):
        rand_pawn, rand_moves = moves_copy.popitem()
        if len(rand_moves) > 0 and state[int(rand_pawn[:1])][int(rand_pawn[2:])] < 0:
            found = True

    rand_move = random.choice(rand_moves)
    print(f"random move from {rand_pawn} to {rand_move}")
    rand_pawn_y = int(rand_pawn[:1])
    rand_pawn_x = int(rand_pawn[2:])
    best_play = (rand_pawn_y, rand_pawn_x), rand_move
    return best_play 