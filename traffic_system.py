
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt


# 1. Generate Synthetic Traffic Data

np.random.seed(42)

n_samples = 200

data = pd.DataFrame({
    "hour": np.random.randint(0, 24, n_samples),
    "day": np.random.randint(0, 7, n_samples),
    "vehicles": np.random.randint(50, 500, n_samples),
    "temperature": np.random.randint(20, 40, n_samples)
})

# Target: congestion level (0–100)
data["congestion"] = (
    data["vehicles"] * 0.15 +
    (data["hour"].apply(lambda x: 1 if 8 <= x <= 10 or 17 <= x <= 19 else 0) * 50) +
    np.random.randint(0, 20, n_samples)
)

data["congestion"] = data["congestion"].clip(0, 100)


# 2. Train ML Model

X = data[["hour", "day", "vehicles", "temperature"]]
y = data["congestion"]

model = RandomForestRegressor()
model.fit(X, y)

# 3. Predict Traffic

def predict_traffic(hour, day, vehicles, temperature):
    input_data = pd.DataFrame([[hour, day, vehicles, temperature]],
                              columns=["hour", "day", "vehicles", "temperature"])
    return model.predict(input_data)[0]


# 4. Pollution Estimation

def estimate_pollution(congestion):
    # simple formula
    co2 = congestion * 0.5   # kg/h
    return co2


# 5. Signal Optimization Logic

def optimize_signal(congestion):
    if congestion > 70:
        return "Increase Green Time (60s)"
    elif congestion > 40:
        return "Moderate Green Time (40s)"
    else:
        return "Reduce Green Time (20s)"


# 6. Run Simulation

print("\n🚦 Smart Traffic Pollution Reducer\n")

hour = int(input("Enter hour (0-23): "))
day = int(input("Enter day (0=Mon ... 6=Sun): "))
vehicles = int(input("Enter number of vehicles: "))
temp = int(input("Enter temperature: "))

predicted_congestion = predict_traffic(hour, day, vehicles, temp)
pollution = estimate_pollution(predicted_congestion)
signal = optimize_signal(predicted_congestion)

print(f"\n📊 Predicted Congestion: {predicted_congestion:.2f}%")
print(f"🌫 Estimated CO₂ Emission: {pollution:.2f} kg/h")
print(f"🚦 Signal Recommendation: {signal}")


# 7. Visualization

plt.bar(["Congestion", "CO2"], [predicted_congestion, pollution])
plt.title("Traffic vs Pollution")
plt.show()
