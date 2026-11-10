HPC Python Homework Project
Social Support and Stress Analysis in a Hypothetical IPV Dataset

Author:K. E. Armstrong-Jacklyn
Date: November, 2026

# IPV Risk-Factor Analysis

## Project Overview

This project examines the relationship between social support and stress using a hypothetical Intimate Partner Violence (IPV) dataset.

The analysis was developed for a reproducible scientific computing workflow using Git, GitHub, GitHub Actions, pytest, and the University of Michigan Great Lakes HPC cluster.

## Research Question

What is the relationship between social support and stress among IPV survivors in a hypothetical dataset?

## Dataset

The program creates a hypothetical dataset containing:

- Participant ID
- Support Score
- Stress Score

No real participant data are used.

## Analysis Performed

The program:

1. Creates a hypothetical IPV dataset.
2. Calculates sample size.
3. Calculates average support scores.
4. Calculates average stress scores.
5. Calculates the correlation between support and stress.
6. Generates a written interpretation.
7. Saves results to `results/ipv_summary.csv`.

## Reproducing the Environment

Create the environment from:

```bash
conda env create -f environment.yml
```

Activate:

```bash
conda activate ipv-analysis-env
```

## Running the Analysis

```bash
python src/main.py
```

## Running Tests

```bash
python -m pytest tests/
```

The test suite verifies:

- dataset size
- average support score
- average stress score
- correlation calculation
- interpretation generation

## Running on Great Lakes

Submit the SLURM batch job:

```bash
sbatch slurm/run_ipv.sh
```

Example completed job:

```text
Job ID: 65806308
State: COMPLETED
ExitCode: 0:0
```

Evidence included:

- logs/job.out
- logs/job.err
- sacct_record.txt

## Results Summary

Results from the analysis:

- Sample Size (N): 10
- Average Support Score: 5.50
- Average Stress Score: 5.30
- Correlation: -0.96

Interpretation:

Individuals with higher social support scores tended to report lower stress scores, indicating that greater social support was associated with lower reported stress levels.

## Repository Contents

- source code (`src/`)
- tests (`tests/`)
- environment file (`environment.yml`)
- SLURM batch script (`slurm/run_ipv.sh`)
- GitHub Actions workflow (`.github/workflows/ci.yml`)
- Great Lakes job logs (`logs/`)
- accounting record (`sacct_record.txt`)
- sample results (`results/ipv_summary.csv`)

## AI Assistance

Microsoft Copilot was used for assistance with:

- project organization
- code refactoring
- pytest development
- GitHub Actions configuration

This project was created for instructional purposes as part of an HPC workflow assignment. The dataset is entirely hypothetical and does not contain real participant information. The analysis is intended to demonstrate reproducible computing practices rather than draw scientific or clinical conclusions.