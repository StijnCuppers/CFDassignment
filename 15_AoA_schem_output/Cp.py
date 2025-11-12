import matplotlib.pyplot as plt
import numpy as np
import os

file_bot = 'postProcessing/sample/0.0295/bottom_p.xy'
file_top = 'postProcessing/sample/0.0295/top_p.xy'

n=0
p_top = np.zeros(40)
p_bot = np.zeros(39)
samples_dir = 'postProcessing/sample'
dirs = [d for d in os.listdir(samples_dir) if os.path.isdir(os.path.join(samples_dir, d))]
for d in dirs:
    top = np.loadtxt(os.path.join(samples_dir, d, 'top_p.xy'))
    bot = np.loadtxt(os.path.join(samples_dir, d, 'bottom_p.xy'))
    p_top += top[:,1]
    p_bot += bot[:,1]
    x_top = top[:,0]
    x_bot = bot[:,0]
    n+=1
avg_p_top = p_top/n
avg_p_bot = p_bot/n

# data_bot = np.loadtxt(file_bot)
# data_top = np.loadtxt(file_top)
# x_bot = data_bot[:, 0]
# x_top = data_top[:, 0]
# p_bot = data_bot[:, 1]
# p_top = data_top[:, 1]

ref_data = np.loadtxt("15_AoA_schem_output/Ref_cp_15deg.dat")
x_over_c = ref_data[:, 0]
Cp_ref = ref_data[:, 1]
x_ref = x_over_c * 1.5

Cp_bot = (avg_p_bot - 46970) / (0.5 * 0.67 * 94.24**2)
Cp_top = (avg_p_top - 46970) / (0.5 * 0.67 * 94.24**2)
plt.figure(figsize=(10, 6))
plt.plot(x_bot, Cp_bot, color='red')
plt.plot(x_top, Cp_top, label='Simulation Cp', color='red')
plt.scatter(x_ref, Cp_ref, label='Reference Cp', color='black', linestyle='--')
plt.xlabel('x [m]')
plt.ylabel('Cp [-]')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("15AoA_cp.png", dpi=300)
plt.show()