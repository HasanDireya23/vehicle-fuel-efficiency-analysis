import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("vehicle_data.csv")


df["timestamp"] = pd.to_datetime(df["timestamp"])


df["fuel_per_km"] = df["fuel_lph"] / df["speed_kmh"]


print("Average Fuel Consumption (L/h):", df["fuel_lph"].mean())
print("Max Fuel Consumption (L/h):", df["fuel_lph"].max())

print("Correlation (Speed vs Fuel):",
      df["speed_kmh"].corr(df["fuel_lph"]))

print("Correlation (RPM vs Fuel):",
      df["rpm"].corr(df["fuel_lph"]))


plt.figure(figsize=(8,5))
plt.plot(df["timestamp"], df["fuel_lph"], marker="o")
plt.title("Fuel Consumption Over Time")
plt.xlabel("Time")
plt.ylabel("Fuel (L/h)")
plt.grid(True)
plt.savefig("fuel_time.png")
plt.show()


plt.figure(figsize=(8,5))
plt.scatter(df["speed_kmh"], df["fuel_lph"])
plt.title("Speed vs Fuel Consumption")
plt.xlabel("Speed (km/h)")
plt.ylabel("Fuel (L/h)")
plt.grid(True)
plt.savefig("speed_vs_fuel.png")
plt.show()


plt.figure(figsize=(8,5))
plt.scatter(df["rpm"], df["fuel_lph"])
plt.title("RPM vs Fuel Consumption")
plt.xlabel("RPM")
plt.ylabel("Fuel (L/h)")
plt.grid(True)
plt.savefig("rpm_vs_fuel.png")
plt.show()
