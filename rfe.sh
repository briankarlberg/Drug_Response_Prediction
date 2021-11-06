#!/bin/bash

#!/bin/bash
#SBATCH --nodes=1
#SBATCH --job-name=sample_response
#SBATCH --time=0-36:00:00
#SBATCH --partition=exacloud
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --output=./output_reports/slurm.%N.%j.out
#SBATCH --error=./error_reports/slurm.%N.%j.err
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=karlberb@ohsu.edu
#SBATCH -a 0-489:1

python CTRPv2_coding_genes_fractional_RFE.py $SLURM_ARRAY_TASK_ID
