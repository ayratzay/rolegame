__author__ = 'AZaynutdinov'



############ settting game #################

from random import randint, sample

players = 2
items = 3

merit = [[randint(1,10) for it in range(items)] for pl in range(players)]

item_ownership = [[args[0] for args in zip(sample([1] + [0] * (players - 1), players))] for i in range(items)]
inventory = [list(args) for args in zip(*item_ownership)]

########### evaluating game results ###############


final_score = [sum([m * i for m, i in zip (mt, iy)]) for mt,iy in zip(merit, inventory)]
all_scores = sorted(list(set(final_score)), reverse = True)


for score in all_scores:
    for index, fs in enumerate(final_score):
        if score == fs:
            print (score,index)


def change_items(A_side, B_side, A_side_item, B_side_item):
    if inventory[A_side][A_side_item]:
        if inventory[B_side][B_side_item]:
            inventory[A_side][A_side_item] = 0
            inventory[B_side][B_side_item] = 0
            inventory[A_side][B_side_item] = 1
            inventory[B_side][A_side_item] = 1
            return inventory[A_side]
    return False

inventory
change_items(0, 0 , 0, 0)

def all_moves(me, others):   # 0, [1]
    """
    returns list of all possible moves for 'me'
    :param me: int
    :param others: list of ints
    :return: list
    """
    possibilities = []
    for my_index, my_item in enumerate(inventory[me]):
        for person in others:
            for others_index, others_item in enumerate(inventory[person]):
                if my_item:
                    if others_item:
                        possibilities.append([me, person, my_index, others_index, change_items]) #at the moment only item exchange
    return possibilities

all_moves(0, [1])

def score_inventory(person, inventory):
    return sum([a*b for a,b in zip(merit[person], inventory)])

score_inventory(0, [1,1,1])
score_inventory(1, [1,1,1])

def evaluate_move(possible_moves):
    """
    Gets all possible turns for player and evaluates utility(merit). Returns the turn with highest utility. If current
    state has most utility returns True
    :param possible_moves: list of list
    :return: list
    """
    possible_moves.append([possible_moves[0][0], possible_moves[0][0], 0, 0, change_items]) # player skips turn
    print [move[-1](*move[0:-1]) for move in possible_moves]


inventory
evaluate_move(all_moves(0, [1]))

def make_turn(move):
    move[-1](*move[0:-1])
    return True

make_turn(move)