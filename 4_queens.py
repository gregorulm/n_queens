"""
4 Queens Problem Solver

Input: any valid board
Output: a board representing a solution, or False

Requires Python 3
"""

import copy

# data definitions
B = False
Q = True
all_positions = range(16)  # a board is defined as a list of length 16

# sample input data

BD0 = [B, B, B, B,
       B, B, B, B,
       B, B, B, B,
       B, B, B, B,]

BD1 = [Q, B, B, B,
       B, B, B, B,
       B, B, B, B,
       B, B, B, B,]

BD2 = [Q, Q, B, B,
       B, Q, B, B,
       B, B, B, B,
       B, B, B, B,]

BD3 = [Q, B, B, B,
       B, B, Q, B,
       B, B, B, B,
       B, B, B, B,]

BD4 = [B, Q, B, B,
       B, B, B, Q,
       Q, B, B, B,
       B, B, Q, B,]

BD5 = [B, Q, B, B,
       B, B, B, B,
       Q, B, B, B,
       B, B, B, B,]

BD6 = [B, B, B, B,
       B, B, B, Q,
       B, B, B, B,
       B, B, B, B,]

BD7 = [B, B, B, B,
       B, B, B, B,
       B, B, B, B,
       B, B, Q, B,]

"""
The following definitions will make it easier to operate on the board.
Ppicture the board with the respective position based on their list index:

  0  1  2  3
  4  5  6  7
  8  9 10 11
 12 13 14 15
 
"""

rows = [ [  0,  1,  2,  3 ],
         [  4,  5,  6,  7 ],
         [  8,  9, 10, 11 ],
         [ 12, 13, 14, 15 ] ]

columns = [ [ 0,  4,  8, 12 ],
            [ 1,  5,  9, 13 ],
            [ 2,  6, 10, 14 ],
            [ 3,  7, 11, 15 ] ]

diagonals = [ [  1,  4 ],
              [  2,  5,  8 ],
              [  3,  6,  9, 12 ],
              [  7, 10, 13 ],
              [ 11, 14 ],
              [  2,  7 ],
              [  1,  6, 11 ],
              [  0,  5, 10, 15 ],
              [  4,  9, 14 ],
              [  8, 13] ]


def visualize(board):
    """
    Input: valid board or False
    Output: string representing squares as "X" and "Q", or False
    """
    if not isinstance(board, list):
        return False
    
    res = ""
    for i in range(len(board)):
        if board[i]:
            res += "Q "
        else:
            res += "X "
        if (i + 1) % 4 == 0 and i < len(board) - 1:
            res += "\n"
    return res

def number_of_queens(board, positions):
    return sum([ 1 for pos in positions if board[pos] ])

def board_valid(board):

    def check_entries(entries):
        for entry in entries:
            if number_of_queens(board, entry) > 1:
                return False
        return True
    
    return all([ check_entries(x) for x in [ rows, columns, diagonals ] ])

def board_solved(board):
    return isinstance(board, list) and board_valid(board) \
            and number_of_queens(board, all_positions) == 4 

# finds all empty squares
def get_positions(board):
    return [ x for x in range(len(board)) if not board[x] ]

def get_next_boards(board, positions):
    result = []
    for pos in positions:
        temp = copy.deepcopy(board)
        temp[pos] = True
        result.append(temp)
    return [ board for board in result if board_valid(board) ]

def solve_board_list(board_list):
    if board_list == []:
        return False
    else:
        check = solve_board(board_list[0])
        if board_solved(check) != False:
            return check
        else:
            return solve_board_list(board_list[1:])

def solve_board(board):
    if board_solved(board):
        return board
    else:
        return solve_board_list(get_next_boards(board, get_positions(board)))

assert solve_board(BD0) == BD4
assert solve_board(BD1) == False
assert solve_board(BD2) == False
assert solve_board(BD3) == False
assert solve_board(BD4) == BD4
assert solve_board(BD5) == BD4
assert solve_board(BD6) == BD4
assert solve_board(BD7) == BD4

#print(visualize(solve_board(BD0)))


"""
#find all solutions:
for i in range(4):
    temp = copy.deepcopy(BD0)
    temp[i] = True
    board = solve_board(temp)
    if isinstance(board, list):
        print(visualize(board), "\n")

"""

"""
#find all valid starting positions:
for i in range(16):
    temp = copy.deepcopy(BD0)
    temp[i] = True
    if isinstance(solve_board(temp), list):
        print(i)
"""
