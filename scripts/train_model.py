import pandas as pd
import mlflow
import sys
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

def train(input_path, output_path, alpha=0.6):
    df = pd.read_csv(input_path)
    X = df.drop("target", axis=1)
    y = df["target"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    model = Ridge(alpha=alpha)
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    mse = mean_squared_error(y_test, preds)

    mlflow.set_experiment("diabetes-regression")
    with mlflow.start_run():
        mlflow.log_param("alpha", alpha)
        mlflow.log_metric("mse", mse)

    
    import joblib
    joblib.dump(model, f"{output_path}/model.pkl")

    
    with open(f"{output_path}/metrics.json", "w") as f:
        f.write(f'{{"mse": {mse}}}')

    print(f"Logged with alpha={alpha}, mse={mse}")

if __name__ == "__main__":
    input_path = sys.argv[1] 
    output_path = sys.argv[2]  
    train(input_path, output_path)