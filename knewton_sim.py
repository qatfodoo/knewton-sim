import pickle
import itertools
from collections import defaultdict

top_users = list(pickle.load( open( "top_users.pkl", "rb" ) ))

top_users_quest = pickle.load( open( "top_users_quest.pkl", "rb" ) )

top_users_perf = pickle.load( open( "top_users_perf.pkl", "rb" ) )

print type(top_users)
print type(top_users_quest)
print type(top_users_perf)

print top_users_quest[350]

avg_err = defaultdict(int) # Avg error of combinations involving question
n_comb = defaultdict(int) # Number of comb having each quest (avoid computing combinatorics (needs unavailable packages))

i = 0
for u in top_users[0:5]:
	i += 1
    print i # Count of users in the loop

    quest = top_users_quest[u].keys()
    top_users_questcomb = list(itertools.combinations(quest, 5))
    user_perf = top_users_perf[u]

   	
    for c in top_users_questcomb:
    	err = (user_perf - 1 / len(c) * sum(c))^2 #quadratic error
    	for q in c:	
	    	avg_err[q] += err
	    	n_comb[q] += 1

	for q in avg_err.keys():
		avg_err[q] /= n_comb[q]

print avg_err
    
