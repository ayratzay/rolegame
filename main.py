__author__ = 'AZaynutdinov'



############ settting game #################

from random import randint, sample
from copy import deepcopy

players = 2
items = 3

merit = [[randint(1,10) for it in range(items)] for pl in range(players)]

item_ownership = [[args[0] for args in zip(sample([1] + [0] * (players - 1), players))] for i in range(items)]
inventory = [list(args) for args in zip(*item_ownership)]

########### evaluating game results ###############


def change_items(A_side, B_side, A_side_item, B_side_item):
    new_state = deepcopy(inventory) # creating new list object # deepcopy works slow
    if inventory[A_side][A_side_item]:
        if inventory[B_side][B_side_item]:
            new_state[A_side][A_side_item] = 0
            new_state[B_side][B_side_item] = 0
            new_state[A_side][B_side_item] = 1
            new_state[B_side][A_side_item] = 1
            return new_state
    return new_state

inventory
change_items(0, 0 , 0, 0)

def all_moves(me, others):   # 0, [1]
    """
    returns list of all possible moves for 'me'
    :param me: int
    :param others: list of ints
    :return: list
    """
    possibilities = [[0,0,0,0, change_items]]   # does nothing
    for my_index, my_item in enumerate(inventory[me]):
        for person in others:
            for others_index, others_item in enumerate(inventory[person]):
                if my_item:
                    if others_item:
                        possibilities.append([me, person, my_index, others_index, change_items]) #at the moment only item exchange
    return possibilities

new_states = [move[-1](*move[0:-1]) for move in all_moves(0, [1])]

first_side_decision = max([(merit[0], state[0]) for state in new_states], key = lambda tpl: sum(m*s for m,s in zip(tpl[0], tpl[1])))


#
# STATE
# PLAYER 0 checks all possible moves
# PLAYER 0 chooses best 3 moves for him
# PLAYER 0 suggests his best deal to conterpart
# conterpart decides if he accetps it or not
# if accepts
#     change
#     next turn
# else:
#     make next valuable suggestion
#

