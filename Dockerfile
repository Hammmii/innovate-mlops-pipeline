FROM python:3.11-slim

WORKDIR /app


RUN apt-get update && apt-get install -y \
    git \
    gcc \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY . .


RUN pip install --upgrade pip && \
    pip install -r requirements.txt -c https://raw.githubusercontent.com/apache/airflow/constraints-3.0.0/constraints-3.11.txt && \
    pip install dvc[gs] mlflow scikit-learn joblib pandas

CMD ["sh", "-c", "dvc repro && tail -f /dev/null"]