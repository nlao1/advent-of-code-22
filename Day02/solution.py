from parse import parse_input

def solution_pt1(filename: str) -> int:
    score = 0
    rps1 = {'A': 'rock', 'B': 'paper', 'C': 'scissors'}
    rps2 = {'X': 'rock', 'Y': 'paper', 'Z': 'scissors'}
    rps_winner = {('rock', 'rock'): 'draw', ('rock', 'paper'): 'win', 
    ('rock', 'scissors'): 'lose', ('paper', 'rock'): 'lose', 
    ('paper', 'paper'): 'draw', ('paper', 'scissors'): 'win', 
    ('scissors', 'rock'): 'win', ('scissors', 'paper'): 'lose', 
    ('scissors', 'scissors'): 'draw'}
    for opp_move, move in parse_input(filename):
        my_move = rps2[move]
        result = rps_winner[(rps1[opp_move], my_move)]
        if my_move == 'rock':
            score += 1
        elif my_move == 'paper':
            score += 2
        elif my_move == 'scissors':
            score += 3

        if result == 'win':
            score += 6
        elif result == 'draw':
            score += 3
    return score

def solution_pt2(filename: str) -> int:
    score = 0
    rps_winning_move = {'rock': 'paper', 'paper': 'scissors', 'scissors': 'rock'}
    rps_losing_move = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}
    rps1 = {'A': 'rock', 'B': 'paper', 'C': 'scissors'}
    for opp_move, desired_result in parse_input(filename):
        opp_move = rps1[opp_move]
        my_move = None
        if desired_result == 'Z': # win
            my_move = rps_winning_move[opp_move]
            score += 6
        elif desired_result == 'X': # lose
            my_move = rps_losing_move[opp_move]
        elif desired_result == 'Y': # draw
            score += 3
            my_move = opp_move
        if my_move == 'rock':
            score += 1
        elif my_move == 'paper':
            score += 2
        elif my_move == 'scissors':
            score += 3
    return score
# print(solution_pt1('example.txt'))
print(solution_pt1('input.txt'))
# print(solution_pt2('example.txt'))
print(solution_pt2('input.txt'))