import os
import re
import sys

# Read arguments
if len(sys.argv) != 2:
    raise ValueError('Please provide a filename input')

filename = sys.argv[1]

# Read file
file_data = open(os.getcwd() + '/' + filename, 'r')

# Parse file
player_1 = []
player_2 = []

flag = 0 # 1 -> player 1, 2 -> player 2
for line in file_data.readlines():
    line = line.replace('\n', '')

    if re.match(r'^Player \d:$', line):
        flag += 1
        continue
    elif line == '':
        continue
    
    if flag == 1:
        player_1.append(int(line))
    else:
        player_2.append(int(line))

# Get answer

def play(player_1, player_2):
    while len(player_1) and len(player_2):
        card_1 = player_1.pop(0)
        card_2 = player_2.pop(0)

        if card_1 > card_2:
            player_1.append(card_1)
            player_1.append(card_2)
        else:
            player_2.append(card_2)
            player_2.append(card_1)

    # Return winner
    if len(player_1):
        return player_1
    else:
        return player_2

winner = play(player_1, player_2)
answer = 0
cards = len(winner)

while cards > 0:
    answer += cards * winner[-cards]
    cards -= 1

print(answer)
