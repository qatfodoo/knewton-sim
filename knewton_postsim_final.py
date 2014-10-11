
import pickle
from collections import defaultdict

sum_err = defaultdict(int)
n_comb = defaultdict(int)

ov_err = 0
ov_it = 0

N_tasks = 10

for t in range(N_tasks):
    sum_err_t = pickle.load(open("./out/sim2/sum_err_task_" + str(t + 1) + ".pkl", "rb"))
    n_comb_t = pickle.load(open("./out/sim2/n_comb_task_" + str(t + 1) + ".pkl", "rb"))
    ov_err_t = pickle.load(open("./out/sim2/ov_err_task_" + str(t + 1) + ".pkl", "rb"))

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
print "Overall error final"
print ov_avg_err

# Restrict to questions with error less than average
final_bank = []
for q in avg_err.keys():
    if avg_err[q] < ov_avg_err:
        final_bank.append(q)

with open('./out/final_bank_sinal.pkl', 'wb') as f:
        pickle.dump(final_bank, f, pickle.HIGHEST_PROTOCOL)

print "Number of questions in final bank"
print len(final_bank)

