import pandas as pd 
import matplotlib.pyplot as plt

data = pd.read_csv("ext_data_log_3.csv")

time = data["seconds_after_power"]
pressure = data["pressure_Pa"]
acceleration_x = data["accel_x_m/s/s"]
acceleration_y = data["accel_y_m/s/s"]
acceleration_z = data["accel_z_m/s/s"]
gyro_x = data["gyro_x_rad/s"]
gyro_y = data["gyro_y_rad/s"]
gyro_z = data["gyro_z_rad/s"]



plt.figure(figsize=(10,5))
plt.plot(time, pressure )
# plt.plot(time, gyro_y, label = "Gyro Y")
# plt.plot(time, gyro_z,label = "Gyro Z" )

# plt.xlim(0, 479)
# plt.ylim(22,38)
plt.title("Pressure as Function of Time ")
plt.xlabel("Time (s)")
plt.ylabel("Pressure (Pa)")


plt.grid(True)
plt.tight_layout()
plt.legend()
plt.show()