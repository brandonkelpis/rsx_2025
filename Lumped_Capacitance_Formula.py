import numpy as np
import matplotlib.pyplot as plt

t_infinity = 403
t_naught = 293
h = 5
density = 1850
specific_heat = 900
area = .1905*.09525
volume  = 0.11938*.1905*0.0016
seconds = np.linspace(0,700,700)
tau = (density*specific_heat*volume) / (h*area)
func = t_infinity + (t_naught-t_infinity)*np.exp((-seconds) /tau )

plt.title("Heating of PCB (Lumped Capacitance Model)", fontsize=10, weight='bold')
plt.xlabel("Time (s)", fontsize=14)
plt.ylabel("Temperature (K)", fontsize=14)
plt.grid(True, linestyle="--", alpha=0.4)
plt.plot (seconds,func,linewidth=1.3)
plt.show()