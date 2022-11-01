from matplotlib import pyplot as plt
import numpy as np


borders = (-4, 4)
x = (-2, -1, 1, 2)
q = (1, -1, 1, 1)

q0 = 1.6 * 10**-19
N = 401

X = np.linspace(*borders, N)
P = np.sum(np.array(q)*q0 / np.abs(np.array(x) - X.reshape(-1, 1)), axis=1)
E = -np.gradient(P, X)

fig, axs = plt.subplots(2, tight_layout=True)
axs[0].plot(X, P)
axs[1].plot(X, E)
plt.show()
