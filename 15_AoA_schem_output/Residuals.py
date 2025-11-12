import numpy as np
import matplotlib.pyplot as plt
import os

path = 'logs'
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
    filepath = os.path.join(path, filename)
    data = np.loadtxt(filepath)
    time = data[:, 0]
    residual = data[:, 1]
    plt.semilogy(time, residual, label=filename.replace("FinalRes0", ""))

plt.xlabel("Time [s]")
plt.ylabel("Residual [SI]")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("residuals.png", dpi=300)
plt.show()
