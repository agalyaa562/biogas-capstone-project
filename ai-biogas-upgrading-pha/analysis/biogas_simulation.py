import numpy as np, pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)
N = 300
CO2_ON, CO2_OFF = 40.0, 35.0
REMOVAL = 0.6   # ASSUMED removal fraction, not measured

rows, stage_on = [], False
for t in range(N):
    raw_co2 = 38 + 5*np.sin(t/40) + np.random.normal(0, 1)   # digester drift
    stage_on = True if raw_co2 > CO2_ON else (False if raw_co2 < CO2_OFF else stage_on)
    out_co2 = raw_co2 * (1 - REMOVAL) if stage_on else raw_co2
    rows.append([t, raw_co2, out_co2, 100 - out_co2, int(stage_on)])

df = pd.DataFrame(rows, columns=["t", "raw_co2", "out_co2", "ch4_est", "stage_on"])
df.to_csv("../data/processed/simulated_run.csv", index=False)

plt.plot(df.t, df.raw_co2, label="Raw CO2 %")
plt.plot(df.t, df.out_co2, label="After upgrading %")
plt.axhline(CO2_ON, ls="--", c="gray", label="ON threshold")
plt.xlabel("Time step"); plt.ylabel("CO2 %"); plt.legend()
plt.title("Simulated threshold control (assumed model)")
plt.savefig("../results/graphs/threshold_control.png", dpi=150)