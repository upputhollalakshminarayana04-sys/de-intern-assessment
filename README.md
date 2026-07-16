# Data Engineer Intern Assessment - Referral Fraud Pipeline

This repository contains a containerized data profiling and processing pipeline built with Python and Pandas to analyze user referral data and flag potential program fraud.

## Project Structure
* `pipeline.py`: Main data execution pipeline (Loads tables, cleans data, applies fraud detection rules, and outputs reports).
* `Dockerfile`: Builds the environment with Python 3.9-slim and project dependencies.
* `requirements.txt`: Manages python packages (`pandas`, `openpyxl`).

## Getting Started

### Prerequisites
* Docker installed on your host machine.

### Execution Instructions
Since the dataset is external, mount your local data folder when running the container.

1. **Build the Docker Image:**
   ```bash docker build -t referral-pipeline .
   
2. **Run the Pipeline (with Volume Mounting):**
   docker run -v "/path/to/your/DE Dataset - intern:/app/data/DE Dataset - intern" -v "$(pwd)/output:/app/output" referral-pipeline

## Fraud Detection Approach
* IP Registration Velocity: Identifies multiple referral accounts registering under an identical IP address to flag potential multi-accounting manipulation.
