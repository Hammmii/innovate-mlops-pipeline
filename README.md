# MLOps Pipeline for Innovate Analytics Inc.

## Project Overview

This project demonstrates the end-to-end **MLOps pipeline** for building, training, deploying, and monitoring machine learning models using best practices and industry-standard tools.

**Key Technologies Used:**
- **DVC (Data Version Control)** for dataset versioning
- **Airflow** for orchestrating ETL and ML pipeline tasks
- **MLflow** for tracking experiments, models, and metrics
- **Docker** for containerizing the application
- **Minikube & Kubernetes** for scalable deployment
- **GitHub Actions** for CI/CD automation

## Project Structure

- **`minikube/`**: Kubernetes deployment files (`deployment.yaml`, `service.yaml`) for Minikube setup
- **`scripts/`**: Python scripts for training and deploying models
- **`Dockerfile`**: Containerizes the application for running on Kubernetes
- **`.github/workflows/ci-cd.yml`**: GitHub Actions workflow for CI/CD pipeline

## How to Run Locally

### 1. Install Dependencies

Ensure you have **Python 3.11** installed, then set up a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate