import pandas as pd, numpy as np
from sklearn.ensemble import IsolationForest

df = pd.read_csv("../data/processed/simulated_run.csv")
df.loc[[80, 150, 220], "raw_co2"] += 15     # injected sensor faults

model = IsolationForest(contamination=0.02, random_state=42)
df["anomaly"] = model.fit_predict(df[["raw_co2"]])
print(df[df.anomaly == -1][["t", "raw_co2"]])