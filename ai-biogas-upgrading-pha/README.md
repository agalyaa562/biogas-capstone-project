# AI-Powered Inline Biogas Upgrading and CO2 Valorization System for PHA Bioplastic Production

Capstone project, Anna University Regional Campus Madurai.

**Team:** S. Agalya, V. Punitha
**Mentor:** Mrs. Vijayalakshmi

## Status

**Software simulation only.** The CO2 removal efficiency (60%) is an assumed
parameter, not a measured value. Real performance needs experimental
validation with a calibrated CH4/CO2 analyser. CO2-to-PHA conversion is a
future research branch and is not demonstrated here.

## What is included

- `firmware/wokwi_esp32/sketch.ino` : ESP32 threshold control with hysteresis (Wokwi simulation)
- `analysis/biogas_simulation.py` : process and control-loop simulation
- `analysis/anomaly_detection.py` : sensor fault detection using Isolation Forest
- `data/processed/simulated_run.csv` : simulated data
- `results/graphs/threshold_control.png` : simulation output graph
- `docs/` : Wokwi screenshot

## How it works

1. Raw biogas CO2 level is read by a sensor (simulated by a potentiometer in Wokwi).
2. ESP32 compares the reading with thresholds: ON above 40%, OFF below 35% (hysteresis).
3. When ON, the upgrading stage reduces CO2 (assumed 60% removal in simulation).
4. Isolation Forest flags abnormal sensor readings (possible leak or sensor fault).

## How to run

    pip install numpy pandas matplotlib scikit-learn
    cd analysis
    python biogas_simulation.py
    python anomaly_detection.py

## Limitations

- All data is simulated. No experimental results are claimed.
- Rule-based control is used now. The AI model is only used for anomaly detection.

## Future work

- Hardware build with real gas sensors and ESP32
- Calibrated CH4/CO2 measurement and real data collection
- AI model training on measured data
- CO2 valorisation study with a biotechnology laboratory