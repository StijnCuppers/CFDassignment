import numpy as np
import matplotlib.pyplot as plt


files = [
    'e_0',
    'k_0',
    'omega_0',
    'p_0',
    'rho_0',
    'Ux_0',
    'Uy_0',
]

plt.figure(figsize=(10,7))

for filename in files:
    data = np.loadtxt(filename)
    time = data[:, 0]
    residual = data[:, 1]
    plt.semilogy(time, residual, label=filename.replace("FinalRes0", ""))

plt.xlabel("Time [s]")
plt.ylabel("Residual")
plt.title("Residuals over Time (rhoPimpleFoam)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()