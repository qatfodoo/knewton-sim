import pickle

top_users = pickle.load( open( "top_users.pkl", "rb" ) )

top_users_quest = pickle.load( open( "top_users_quest.pkl", "rb" ) )

top_users_perf = pickle.load( open( "top_users_perf.pkl", "rb" ) )

print top_users_quest[350]