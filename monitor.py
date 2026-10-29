from sklearn.datasets import load_diabetes
import pandas as pd
from evidently import Report
from evidently.presets import DataDriftPreset

data = load_diabetes()

df = pd.DataFrame(
    data.data,
    columns=data.feature_names
)

reference_data = df.iloc[:220].copy()
current_data = df.iloc[220:].copy()

# Simulate data drift
current_data["bmi"] += 0.5

report = Report([DataDriftPreset()])

result = report.run(
    reference_data=reference_data,
    current_data=current_data
)

result.save_html("diabetes_drift_report.html")

print("Diabetes data monitoring completed.")
print("Report saved as diabetes_drift_report.html")