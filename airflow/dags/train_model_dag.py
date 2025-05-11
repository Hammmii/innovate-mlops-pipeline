from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import subprocess

def run_model_training(**kwargs):
    subprocess.run(["python", "/Users/apple.store.pk/Desktop/MLOps_Project/scripts/train_model.py"], check=True)

with DAG(
    'model_training_dag',
    default_args={
        'owner': 'airflow',
        'retries': 1,
    },
    description='Train a model with Airflow',
    schedule_interval="* * * * *",  # Runs every minute
    start_date=datetime(2025, 5, 10),
    catchup=False,
) as dag:

    train_model_task = PythonOperator(
        task_id='train_model_task',
        python_callable=run_model_training,
    )

    train_model_task