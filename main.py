__author__ = 'AZaynutdinov'



############ settting game #################

from random import randint, sample
from copy import deepcopy

players = 3
items = 4

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

def all_moves(me, other):   # 0, 1
    """
    returns list of all possible moves for 'me'
    :param me: int
    :param others: int
    :return: list
    """

    for my_index, my_item in enumerate(inventory[me]):
        if my_item:
            for others_index, others_item in enumerate(inventory[other]):
                if others_item:
                    yield ([me, other], [my_index, others_index, change_items])


def evaluate_state(state, who):
    new_state_merit = [sum([i*im for i,im in zip(sl,ml)]) for sl,ml in zip(state, merit)]
    return make_decision(stage_merit, new_state_merit, who)

def make_decision(old_state, new_state, who):
    g = range(players)
    g.remove(who)
    d_who_merit = new_state[who] - old_state[who]
    d_others_merit = sum([new_state[p] - old_state[p] for p in g])/2
    return  d_who_merit -  d_others_merit #returns score for state for sorting


def player_turn(me, others):
    result = []
    g = range(others)
    g.remove(me)
    for othr_player in g:
        for side, params in  all_moves(0, othr_player):
            ns = params[-1](*(side + params[0:-1]))
            if evaluate_state(ns, me) > 0:
                print evaluate_state(ns, me)
                result.append(ns)
    return result

me = 0
new_states =  player_turn(me, players)
sorted_new_states = sorted(new_states, key=lambda x: evaluate_state(x, me), reverse=True)

for i in sorted_new_states:
    print evaluate_state(i, me)


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

