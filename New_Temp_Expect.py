import numpy as np
import matplotlib.pyplot as plt
import scienceplots
from scipy.integrate import dblquad
plt.style.use (['science', 'notebook', 'grid'])
from numba import njit 

@njit
def integrand (t):
  density = 0.6565
  velocity = -28.47*(t-376)+1629
  drag = 1
  area = 1.905e-5
  return (1/2)*density*(velocity**3)*drag*area

t1 = 376.0
t2 = 427.0

E_drag, error = dblquad(integrand, t1, t2)

print("Drag energy [J]:", E_drag)
print("quad error estimate:", error)