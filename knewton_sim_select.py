import pickle
import random
from collections import defaultdict
import os
import time
import math

if os.getenv('SLURM_JOB_ID') != "":
    #task_id = int(os.getenv('SLURM_ARRAY_TASK_ID')) # Task id, to parallelize computation
    task_id = 10
    print task_id
    start_time = time.time()

    # Load top users data
    top_users = list(pickle.load(open("top_users.pkl", "rb")))
    top_users_quest = pickle.load(open("top_users_quest.pkl", "rb"))
    top_users_perf = pickle.load(open("top_users_perf.pkl", "rb"))

    N_tasks = 10 # Number of parallel tasks
    M = 10000 # Number of simulations

    # Load questions ordered by scoring error in previous simulation
    sorted_quest = pickle.load(open("./out/sorted_quest.pkl", "rb")) # tuple
    max_ind = int(math.floor(len(sorted_quest) * (0.5 + float(task_id) / 2 / N_tasks))) # From 50% to all questions.
    print max_ind
    print 
    print len(sorted_quest)
    final_bank = [t[0] for t in sorted_quest][0:max_ind]

    sum_err = defaultdict(int) # Avg error of combinations involving question
    n_comb = defaultdict(int) # Number of comb having each quest (avoid computing combinatorics (needs unavailable packages))

    ov_err = 0 # Overall avg error on all simulations
    ov_it = 0
    for i in range(len(top_users)):

        u = top_users[i]
        quest = list(set(top_users_quest[u].keys()) & set(final_bank)) # Intersection of user's questions and final bank
        user_perf = top_users_perf[u][0]

        for b in range(M):
            c = random.sample(quest, 5)
            err = (user_perf - 1 / float(len(c)) * float(sum([top_users_quest[u][q] for q in c]))) ** 2 # quadratic error
            ov_err += err
            ov_it += 1

            for q in c: 
                sum_err[q] += err
                n_comb[q] += 1


    with open('./out/sim2/ov_err_sorted_task_' + str(task_id) + '.pkl', 'wb') as f:
        pickle.dump((ov_err, ov_it), f, pickle.HIGHEST_PROTOCOL)

    print("--- %s seconds ---" % str(time.time() - start_time)) # Program time
