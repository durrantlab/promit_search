#!/bin/bash
#SBATCH --job-name=pharm_search
#SBATCH --cluster=smp
#SBATCH --partition=preempt
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=4G
#SBATCH --time=12:00:00
#SBATCH --output=test.out

module purge
module load pixi

line 1
line 2
line 3