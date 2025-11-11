import matplotlib.pyplot as plt
import numpy as np

file_bot = 'postProcessing/sample/1.1/bottom_p.xy'
file_top = 'postProcessing/sample/1.1/top_p.xy'

data_bot = np.loadtxt(file_bot)
data_top = np.loadtxt(file_top)
x_bot = data_bot[:, 0]
x_top = data_top[:, 0]
p_bot = data_bot[:, 1]
p_top = data_top[:, 1]

ref_data = np.loadtxt("Coarse_Output/Ref_cp_0deg.dat")
x_over_c = ref_data[:, 0]
Cp_ref = ref_data[:, 1]
x_ref = x_over_c * 1.5

Cp_bot = (p_bot - 46970) / (0.5 * 0.67 * 94.24**2)
Cp_top = (p_top - 46970) / (0.5 * 0.67 * 94.24**2)
plt.figure(figsize=(10, 6))
plt.plot(x_bot, Cp_bot, color='red')
plt.plot(x_top, Cp_top, label='Simulation Cp', color='red')
plt.plot(x_ref, Cp_ref, label='Reference Cp', color='black', linestyle='--')
plt.xlabel('x [m]')
plt.ylabel('Cp [-]')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


