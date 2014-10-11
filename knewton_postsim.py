import pickle
from collections import defaultdict
import operator

sum_err = defaultdict(int)
n_comb = defaultdict(int)

ov_err = 0
ov_it = 0

N_tasks = 10

for t in range(N_tasks):
    sum_err_t = pickle.load(open("./out/sim1/sum_err_task_" + str(t + 1) + ".pkl", "rb"))
    n_comb_t = pickle.load(open("./out/sim1/n_comb_task_" + str(t + 1) + ".pkl", "rb"))
    ov_err_t = pickle.load(open("./out/sim1/ov_err_task_" + str(t + 1) + ".pkl", "rb"))

    for q in sum_err_t:
        sum_err[q] += sum_err_t[q]
    for q in n_comb_t:
        n_comb[q] += n_comb_t[q]

    ov_err += ov_err_t[0]
    ov_it += ov_err_t[1]

avg_err = {}
for q in sum_err.keys():
    avg_err[q] = sum_err[q] / n_comb[q]

ov_avg_err = ov_err / ov_it
print "Overall error"
print ov_avg_err

# Get list of questions, sorted by avg error
sorted_quest = sorted(avg_err.items(), key=operator.itemgetter(1))

print sorted_quest
with open('./out/sorted_quest.pkl', 'wb') as f:
        pickle.dump(sorted_quest, f, pickle.HIGHEST_PROTOCOL)

