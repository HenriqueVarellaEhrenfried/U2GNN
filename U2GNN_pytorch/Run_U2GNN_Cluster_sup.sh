#!/bin/bash

#SBATCH -t 7-00:00:00
#SBATCH --cpus-per-task=32
#SBATCH -o U2GNN_SPACY_Ohsumed.log
#SBATCH --job-name=hve_U2GNN
#SBATCH -p 7d
#SBATCH -n 1
#SBATCH -N 1

source $HOME/.virtualenvs/U2GNN/bin/activate

python -V

pwd

srun time python script_experiments_sup.py