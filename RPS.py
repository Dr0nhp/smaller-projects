# This is a simple game of Rock Paper scissor
# At first it is played naive
# After that some statistics from the running game should be implemented
# After the statistics are in an 'ai' should be able to use these

# R = 82  (Ascii value)
# P = 80
# S = 83
# Paper beats Rock -> -> ->       P-S = -2
# Scissor beats Paper ->->->      S-P =  3
# Rock beats Scissor              R-S = -1


import random

def winning_condition(a, b):
    i = a - b
    if i == -2 and a == 80:
        return 1

    elif i == 3 and a == 83:
        return 1

    elif i == -1 and a == 82:
        return 1

    elif i == 0:
        return 2

    else:
        return 0

def game(a, b, c):
    if winning_condition(a, b) == 1:
        print("You won!")
        c[0] += 1
    elif winning_condition(a, b) == 2:
        print("Draw!")
        c[1] += 1
    else:
        print("You Lose!")
        c[2] += 1
    return c


def statistics(x,y):
    x_arith = abs((y[0] / x) * 100)
    print('\n', y[0], 'wins\n', y[1], 'draws\n', y[2], 'loses\n')
    print('You had a winning rate of: ', x_arith, '%\n')


number_of_games = int(input("Number of games you want to play\n"))
x = number_of_games
stats_array = [0, 0, 0]

while x > 0:
    user_value = ord(input("RPS\n"))
    generated_value = ord(random.choice(["R", "P", "S"]))
    game(user_value, generated_value, stats_array)
    x -= 1
    print(x, "rounds to play\n")
statistics(number_of_games,stats_array)
input("Press to exit")