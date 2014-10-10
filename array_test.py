import os

if os.getenv('SLURM_JOB_ID') != "":
    print os.getenv('SLURM_ARRAY_TASK_ID')
