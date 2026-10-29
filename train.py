from sklearn.datasets import load_diabetes
from sklearn.ensemble import RandomForestRegressor
import joblib

data = load_diabetes()

X = data.data
y = data.target

model = RandomForestRegressor(
    n_estimators=50,
    random_state=42
)

model.fit(X, y)

joblib.dump(model, "diabetes_model.pkl")

print("Diabetes model trained successfully.")