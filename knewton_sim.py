import pickle
import itertools
import random
from collections import defaultdict
import os

if os.getenv('SLURM_JOB_ID') != "":
    task_id = int(os.getenv('SLURM_ARRAY_TASK_ID')) # Task id, to parallelize computation
    # Load top users data
    top_users = list(pickle.load( open( "top_users.pkl", "rb" ) ))
    top_users_quest = pickle.load( open( "top_users_quest.pkl", "rb" ) )
    top_users_perf = pickle.load( open( "top_users_perf.pkl", "rb" ) )

    N_tasks = 10 # Number of parallel tasks
    M = 100000 # Number of simulations per top users

    sum_err = defaultdict(int) # Avg error of combinations involving question
    n_comb = defaultdict(int) # Number of comb having each quest (avoid computing combinatorics (needs unavailable packages))

    ov_err = 0 # Overall avg error on all simulations
    ov_it = 0
    for i in range(len(top_users)):

        if i % N_tasks != (task_id - 1): continue # Only consider 1/10 of users per task

        u = top_users[i]
        quest = top_users_quest[u].keys()
        user_perf = top_users_perf[u][0]

        for b in range(M):
            c = random.sample(quest, 5)
            err = (user_perf - 1 / float(len(c)) * float(sum([top_users_quest[u][q] for q in c]))) ** 2 # quadratic error
            ov_err += err
            ov_it += 1

            for q in c:	
                sum_err[q] += err
                n_comb[q] += 1


    with open('./out/sum_err_task_' + str(task_id) + '.pkl', 'wb') as f:
        pickle.dump(sum_err, f, pickle.HIGHEST_PROTOCOL)

    with open('./out/n_comb_task_' + str(task_id) + '.pkl', 'wb') as f:
        pickle.dump(n_comb, f, pickle.HIGHEST_PROTOCOL)

    with open('./out/ov_err_task_' + str(task_id) + '.pkl', 'wb') as f:
        pickle.dump((ov_err, ov_it), f, pickle.HIGHEST_PROTOCOL)
