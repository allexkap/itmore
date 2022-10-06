from matplotlib import pyplot as plt
import numpy as np


v0 = 1000
B0 = 10**-2
q0 = 1.6 * 10**-19
m0 = 1.66 * 10**-27
ms = [i for i in range(20, 25)]

dt = 10**-6
N = 10**2

n = len(ms)
m = np.array([ms]).T * m0
x = np.zeros((N, n, 3))
v = np.zeros((n, 3))
B = np.zeros(3)

v[:, 1] = v0
B[2] = B0

for i in range(1, N):
    x[i] = x[i-1] + (v := v + q0 * np.cross(v, B) / m * dt) * dt

plt.plot(x[:, :, 0], x[:, :, 1], '-', label=tuple(f'{m} Da' for m in ms))
plt.legend()
plt.show()
