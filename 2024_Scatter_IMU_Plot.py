import pandas as pd 
import matplotlib.pyplot as plt

data = pd.read_csv("2025 Temp + IMU of payload.xlsx - sensor_data.csv")

time = data["Timestamp Seconds"]
temp = data["temp"]        

plt.figure(figsize=(10,5))
plt.scatter(time, temp)
plt.xlim(0, 479)
plt.ylim(22,38)
plt.title("Temperature vs Time")
plt.xlabel("Time (s)")
plt.ylabel("Temperature ($^\circ$C)")

plt.grid(True)
plt.tight_layout()
plt.show()
