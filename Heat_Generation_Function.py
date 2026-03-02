import numpy as np
import matplotlib.pyplot as plt

power_without_battery = 18.1
mols = 0.86
cv = 20.8
intial_temperature = 297 
power_with_battery = 20.1
mols_x_cv = mols * cv
no_batt_frac = power_without_battery / mols_x_cv

seconds = np.linspace(0,600,600)
with_batt_frac = power_with_battery / mols_x_cv
with_batt_whole_func = (with_batt_frac*seconds) + intial_temperature
no_batt_whole_func = (no_batt_frac*seconds) + intial_temperature
function_without_battery = no_batt_whole_func
function_with_battery = with_batt_whole_func

no_battery_cutoff = np.argmax(seconds > 336)

plt.plot(seconds[:no_battery_cutoff],function_without_battery[:no_battery_cutoff], label = 'Without Battery', color = 'blue')
plt.plot(seconds[no_battery_cutoff:], function_with_battery[no_battery_cutoff:],label='With Battery', color='red')
plt.xlabel("Time (s)")
plt.ylabel("Temperature (K)")
plt.legend(fontsize=15)
plt.grid(True)
plt.show()

