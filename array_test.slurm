#!/bin/bash
#SBATCH -J array-test # name for job array
#SBATCH -o ./dump/array_test.out #Standard output
#SBATCH -e ./dump/array_test.err #Standard error
#SBATCH -p general #Partition
#SBATCH -t 02:00:00 #Running time of 20 mins.
#SBATCH --mem-per-cpu 3000 #Memory request
#SBATCH -n 1 #Number of cores
#SBATCH -N 1 #All cores on one machine
#SBATCH --mail-user=kuatefodouop@fas.harvard.edu
#SBATCH --mail-type=ALL    # When to send mail

# argument = job id

python array_test.py $SLURM_ARRAY_TASK_ID
