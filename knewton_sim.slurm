#!/bin/bash
#SBATCH -J knewton-sim # name for job array
#SBATCH -o ./dump/ksim.out #Standard output
#SBATCH -e ./dump/ksim.err #Standard error
#SBATCH -p general #Partition
#SBATCH -t 02:00:00 #Running time of 20 mins.
#SBATCH --mem-per-cpu 8000 #Memory request
#SBATCH -n 1 #Number of cores
#SBATCH -N 1 #All cores on one machine
#SBATCH --mail-user=kuatefodouop@fas.harvard.edu
#SBATCH --mail-type=ALL    # When to send mail


python knewton_sim.py
