import pickle
import itertools
import random
from collections import defaultdict

top_users = list(pickle.load( open( "top_users.pkl", "rb" ) ))

top_users_quest = pickle.load( open( "top_users_quest.pkl", "rb" ) )

top_users_perf = pickle.load( open( "top_users_perf.pkl", "rb" ) )

M = 10000 # Number of simulations per top users

avg_err = defaultdict(int) # Avg error of combinations involving question
n_comb = defaultdict(int) # Number of comb having each quest (avoid computing combinatorics (needs unavailable packages))

ov_err = 0 # Overall avg error on all simulations
ov_it = 0
for u in top_users:

    quest = top_users_quest[u].keys()
    user_perf = top_users_perf[u][0]

    for b in range(M):
    	c = random.sample(quest, 5)
    	err = (user_perf - 1 / float(len(c)) * float(sum([top_users_quest[u][q] for q in c]))) ** 2 # quadratic error
        ov_err += err
        ov_it += 1

    	for q in c:	
	    	avg_err[q] += err
	    	n_comb[q] += 1



for q in avg_err.keys():
	avg_err[q] /= n_comb[q]

print avg_err

print "Overall avg error"
print ov_err / ov_it