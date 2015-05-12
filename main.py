__author__ = 'AZaynutdinov'



############ settting game #################

from random import randint, sample

players = 10
items = 22

merit = [[randint(1,10) for it in range(items)] for pl in range(players)]

item_ownership = ([args[0] for args in zip(sample([1] + [0] * (players - 1), players))] for i in range(items))
inventory = [args for args in zip(*item_ownership)]

########### evaluating game results ###############


final_score = [sum([m * i for m, i in zip (mt, iy)]) for mt,iy in zip(merit, inventory)]
all_scores = sorted(list(set(final_score)), reverse = True)


for score in all_scores:
    for index, fs in enumerate(final_score):
        if score == fs:
            print (score,index)