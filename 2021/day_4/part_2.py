import os
import re
import sys

# Read arguments
if len(sys.argv) != 2:
    raise ValueError('Please provide a filename input')

filename = sys.argv[1]

# Read file
file_data = open(os.getcwd() + '/' + filename, 'r')

#
# Parse file
#
text = file_data.read()

# Split by empty lines
parts = text.split('\n\n')
draw = map(int, parts[0].split(','))

# List of boards (matrix)
boards = []

for part in parts[1:]:
    matrix = []
    h_lines = part.split('\n')
    h_lines = [l for l in h_lines if l]

    for h_line in h_lines:
        h_l = re.split('\s+', h_line)
        h_l = [(int(v), False) for v in h_l if v]
        matrix.append(h_l)

    boards.append(matrix)

#
# Get answer
#

def mark_number(boards, n):
    for b in range(len(boards)):
        for h in range(len(boards[b])):
            for v in range(len(boards[b][h])):
                if boards[b][h][v][0] == n:
                    boards[b][h][v] = (n, True)

def get_board_loosers(boards):
    boards_loosers = []
    lines_per_row = len(boards[0][0])

    for board in boards:
        winner = False

        # Check horizontally
        for h_line in board:
            winner = all(v[1] for v in h_line)

            if winner:
                break

        # Check vertically
        if not winner:
            for v_index in range(lines_per_row):
                v_line = []

                for h_line in board:
                    v_line.append(h_line[v_index])

                winner = all(v[1] for v in v_line)

                if winner:
                    break

        if not winner:
            boards_loosers.append(board)

    return boards_loosers

# Do the draw
last_board_winner = None
boards_loosers = []
last_boards_loosers = []
last_number = None
lines_per_row = len(boards[0][0])

for i, number in enumerate(draw):
    mark_number(boards=boards, n=number)

    # To some board be the winner we need to draw at least the quantity
    # of numbers per line
    if i + 1 >= lines_per_row:
        boards_loosers = get_board_loosers(boards)

        if len(last_boards_loosers) > 0 and len(boards_loosers) == 0:
            last_board_winner = last_boards_loosers[-1]
            last_number = number
            break

    last_boards_loosers = boards_loosers

# Calculate result from the board winner
sum_unmarked_numbers = 0

for h_line in last_board_winner:
    for v in h_line:
        if not v[1]:
            sum_unmarked_numbers += v[0]

answer = last_number * sum_unmarked_numbers
print(answer)
