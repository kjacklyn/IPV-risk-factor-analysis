#!/bin/bash

#SBATCH --job-name=ipv_project
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=2G
#SBATCH --time=00:10:00
#SBATCH --output=logs/job.out
#SBATCH --error=logs/job.err

python src/main.py