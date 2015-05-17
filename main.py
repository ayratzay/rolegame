__author__ = 'AZaynutdinov'



############ settting game #################

from random import randint, sample
from copy import deepcopy
from math import exp
from operator import itemgetter
from random import uniform

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

def all_moves(me, other):
    for my_index, my_item in enumerate(inventory[me]):
        if my_item:
            for others_index, others_item in enumerate(inventory[other]):
                if others_item:
                    for func in [change_items]:
                        yield ([me, other], [my_index, others_index, func])

def eval_move(move):
    s, p = move
    new_state = p[-1](s[0], s[1], *p[:-1])
    new_state_merit = [sum([i*im for i,im in zip(sl,ml)]) for sl,ml in zip(new_state, merit)]
    return new_state_merit[s[0]] - stage_merit[s[0]]

def sigmoid(num, max):
    x = float(num)/max
    left_shit = 0.5  #decrease to shit left
    return 1/(1+exp(-6*(x-left_shit)))

def eval_proposal(move):
    s, p = move
    d_utility_me = eval_move(move)
    d_utility_other = eval_move([s[::-1], p[:-1][::-1]+[p[-1]]])
    d_utility_other_max = max([eval_move(m) for pl in range(players) for m in all_moves(s[-1], pl) if s[-1] != pl])
    utility = d_utility_me * sigmoid(d_utility_other, d_utility_other_max)
    if utility < 0:
        utility = 0
    return (move, utility)

def make_decision(ml):
    rnd = uniform(0,sum([m[1] for m in ml]))
    return [i for i in ml if i[1] > rnd][-1]
##############FIRST EPOCH#################

proposal_pool = []
for p1 in range(players):
    moves = sorted([eval_proposal(move) for p2 in range(players) if p1 != p2
                  for move in all_moves(p1, p2) if eval_proposal(move)[1] > 0.5], key=itemgetter(1), reverse=True)
    if len(moves):
        proposal_pool.append(make_decision(moves))


##############SECOND EPOCH##############

for pr in proposal_pool:
    (s, m), p = pr
    n_sm = eval_move([s[::-1]]+ [m[1::-1] +[ m[-1]]])
    max_sm = max([eval_move(moves) for pl in range(players) for moves in all_moves(*[s[1]]+ [pl]) if s[-1] != pl])

    n_sm * sigmoid(n_sm, max_sm)
    #make decision if accept proposal or make own propposal

#second_epoch:
for player in all_players:
    if purpose[1] == player:
        if evaluate_purpose() == 'reject'
            add_rejected_pool
        if evaluate_purpose() == 'postponed'
            add_postponed_pool
        if evaluate_purpose() == 'accepted'
            add_to_execute_pool
#evaluation_epoch:
make moves