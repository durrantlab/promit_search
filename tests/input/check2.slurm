#!/bin/bash
#SBATCH --job-name=pharm_search
#SBATCH --cluster=smp
#SBATCH --partition=preempt
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=4G
#SBATCH --time=12:00:00
#SBATCH --output=logs/%A_%a.out
#SBATCH --error=logs/%x_%A_%a.err

module purge
module load pixi

ARGS=$(awk -v line=$((SLURM_ARRAY_TASK_ID + 1)) 'NR == line {print $0}' "job_list.txt")
LOG="${OUT%.sdf}.log
$ARGS | tee "$LOG"
echo "Done!"