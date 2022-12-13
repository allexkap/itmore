from matplotlib import pyplot as plt
import numpy as np


c = 3 * 10**8
v = c * 0.1
y = 1

def dopler_cl(u):
    return 1 / (1 - u/c)
def dopler_rl(u):
    return dopler_cl(u) * (1-(v/c)**2)**.5

x = np.linspace(-2, 2, 1001)
u = v * -x/(x**2+y**2)**.5

plt.rcParams['axes.formatter.use_mathtext'] = True
plt.rcParams['axes.formatter.limits'] = (0, 0)
plt.figure(tight_layout=True)
plt.plot(x, dopler_cl(u)-1, label='classical')
plt.plot(x, dopler_rl(u)-1, label='relativistic')
plt.xlabel('$x$, m')
plt.ylabel('$\\nu$ / $\\nu_0$')
plt.legend(loc=3)
plt.grid()
plt.show()
