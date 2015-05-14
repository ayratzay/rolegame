__author__ = 'AZaynutdinov'



############ settting game #################

from random import randint, sample
from copy import deepcopy

players = 2
items = 3

merit = [[randint(1,10) for it in range(items)] for pl in range(players)]

_item_ownership = [[args[0] for args in zip(sample([1] + [0] * (players - 1), players))] for i in range(items)]
inventory = [list(args) for args in zip(*_item_ownership)]
stage_merit = [sum([i*m for i,m in zip(pi, pm)]) for pi,pm in zip(inventory, merit)]





########### evaluating game results ###############
########## Works only for NUMBER ONE Player #######
##################################################


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
    possibilities = []   # does nothing
    for my_index, my_item in enumerate(inventory[me]):
        for person in others:
            for others_index, others_item in enumerate(inventory[person]):
                if my_item:
                    if others_item:
                        possibilities.append([me, person, my_index, others_index, change_items]) #at the moment only item exchange
    return possibilities

def evaluate_state(state):
    new_state_merit = [sum([i*im for i,im in zip(sl,ml)]) for sl,ml in zip(state, merit)]
    return make_decision(stage_merit, new_state_merit)

def make_decision(old_state, new_state):
    return (new_state[0] - old_state[0]) - (sum(new_state[1:]) - sum(old_state[1:]))/2   #returns score for state for sorting


new_states = [move[-1](*move[0:-1]) for move in all_moves(0, [1]) if evaluate_state(move[-1](*move[0:-1])) > 0]
sorted_new_states = sorted(new_states, key=evaluate_state)





#
# STATE OK
# PLAYER 0 checks all possible moves OK
# PLAYER 0 chooses best 3 moves for him OK
# PLAYER 0 suggests his best deal to conterpart OK
# conterpart decides if he accetps it or not   TODO
# if accepts
#     change
#     next turn
# else:
#     make next valuable suggestion
#

