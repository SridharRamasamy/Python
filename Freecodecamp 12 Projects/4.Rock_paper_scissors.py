# # Project 4:
# # Rock paper scissors 
import random
def play():
    user = input (" 'r' for rock, 'p' for paper, 's' for scissors : ")
    Computer = random.choice(['r','p','s'])
    if user == Computer:   #  r > s, s > p, p > r
        return 'tie'
    if is_win(user,Computer): 
        return 'Your Won'
    if is_loss(user,Computer): 
        return 'Your Loss'

def is_win(player, opponent):
    # return True if player wins
    #  r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

def is_loss(player, opponent):
    # return True if player wins
    #  r > s, s > p, p > r
    if (player == 's' and opponent == 'r') or (player == 'p' and opponent == 's') or (player == 'r' and opponent == 'p'):
        return True
print(play())

# # or

import random
def play():
    user = input (" What's your choice? \n 'r' for rock, 'p' for paper, 's' for scissors : ")
    Computer = random.choice(['r','p','s'])
    if user == Computer:   #  r > s, s > p, p > r
        return 'tie'
    if is_win(user,Computer): 
        return 'Your Won'
    else : 
        return 'Your Loss'

def is_win(player, opponent):
    # return True if player wins
    #  r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
print(play())

# # or

import random
def play():
    user = input (" 'r' for rock, 'p' for paper, 's' for scissors : ")
    Computer = random.choice(['r','p','s'])
    if user == Computer:   #  r > s, s > p, p > r
        return 'tie'
    if (user == 'r' and Computer == 's') or (user == 's' and Computer == 'p') or (user == 'p' and Computer == 'r'):
        return 'Your Won'
    if (user == 's' and Computer == 'r') or (user == 'p' and Computer == 's') or (user == 'r' and Computer == 'p'):
        return 'Your Loss'
print(play())