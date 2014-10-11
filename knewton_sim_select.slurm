#!/bin/bash
#SBATCH -J knewton-sim # name for job array
#SBATCH -o ./dump/ksim_select.out #Standard output
#SBATCH -e ./dump/ksim_select.err #Standard error
#SBATCH -p general #Partition
#SBATCH -t 02:00:00 #Running time of 2 hours.
#SBATCH --mem-per-cpu 10000 #Memory request 10 GB
#SBATCH -n 1 #Number of cores
#SBATCH -N 1 #All cores on one machine
#SBATCH --mail-user=kuatefodouop@fas.harvard.edu
#SBATCH --mail-type=ALL    # When to send mail


python knewton_sim_select.py
