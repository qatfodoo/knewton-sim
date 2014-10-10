import pickle
import itertools
from collections import defaultdict

top_users = list(pickle.load( open( "top_users.pkl", "rb" ) ))

top_users_quest = pickle.load( open( "top_users_quest.pkl", "rb" ) )

top_users_perf = pickle.load( open( "top_users_perf.pkl", "rb" ) )

## Tentative to generate all 5 questions combination.
# Aborted because too intense computationally (memory limits).

avg_err = defaultdict(int) # Avg error of combinations involving question
n_comb = defaultdict(int) # Number of comb having each quest (avoid computing combinatorics (needs unavailable packages))

i = 0
for u in top_users:
    i += 1
    print i # Count of users in the loop

    quest = top_users_quest[u].keys()
    top_users_questcomb = list(itertools.combinations(quest, 5))
    user_perf = top_users_perf[u]

    print user_perf
    
    for c in top_users_questcomb:
    	err = (user_perf - 1 / len(c) * float(sum(c))) ** 2 # quadratic error
    	for q in c:	
	    	avg_err[q] += err
	    	n_comb[q] += 1

	for q in avg_err.keys():
		avg_err[q] /= n_comb[q]

print avg_err
    
