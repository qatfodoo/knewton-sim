import pickle
import itertools

top_users = list(pickle.load( open( "top_users.pkl", "rb" ) ))

top_users_quest = pickle.load( open( "top_users_quest.pkl", "rb" ) )

top_users_perf = pickle.load( open( "top_users_perf.pkl", "rb" ) )

print type(top_users)
print type(top_users_quest)
print type(top_users_perf)

print top_users_quest[350]

i = 0
for u in top_users[0:5]:
    quest = top_users_quest[u].keys()
    top_users_questcomb = list(itertools.combinations(quest, 5))
    i += 1
    print i
    if i > 10:
    	break
