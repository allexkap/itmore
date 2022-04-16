from matplotlib import pyplot as plt
import itertools as it
import numpy as np

# EDIT
VAR = 'm0'
ONCE = 1

# PARAMS
DIM = (2, 2)
NAME = 'Jet propulsion simulation'
AXES = (('x(t)', 'v(t)', 'a(t)'), ('p(t)', 'm(t)', 'F(t)'))
VARS = {'m0': 'm_0', 'm1': 'm_1', 'alpha': '\\alpha', 'k': 'k', 'flow': 'v_i'}
AXIS = ((('с', 'м'), ('с', 'м/с'), ('с', 'м/с$^2$')), (('с', 'м$\\cdot$кг/c'), ('с', 'кг'), ('с', 'Н')))
ADJ = {'top': 0.922, 'bottom': 0.081, 'left': 0.054, 'right': 0.972, 'hspace': 0.356, 'wspace': 0.190}
LIM = (((100, 5*10**5), (100, 25*10**3)), ((100, 4*10**10), (100, 2*10**7)))
plt.rcParams['axes.formatter.use_mathtext'] = True
plt.rcParams['axes.formatter.limits'] = [-2, 3]
BETA = tuple(1+(i//2+1)/10*(i%2*2-1) for i in range(10))
O = tuple(5+((i//2+1)*(i%2*2-1)+6*(not i-10)) for i in range(11))

# CREATE
Lines = []
fig = plt.figure(label=NAME, figsize=(6.4*(DIM[0]/DIM[1]), 4.8*(1+0.15*(not ONCE))), tight_layout=0)
if not ONCE: ADJ['bottom'] = 1-(1-ADJ['bottom'])/1.15
fig.subplots_adjust(**ADJ)
Axes = fig.subplots(DIM[1], DIM[0])
for i, j in it.product(range(DIM[1]), range(DIM[0])):
    Axes[i][j].set_title(AXES[i][j])
    if ONCE:
        Axes[i][j].grid(alpha=0.4)
        Axes[i][j].set_xlim(0, LIM[i][j][0])
        Axes[i][j].set_ylim(0, LIM[i][j][1])
for i, j, k in it.product(range(DIM[1]), range(DIM[0]), range(2)):
    Axes[i][j].text((0.97, 0.035)[k], (0.045, 0.95)[k], f' {AXIS[i][j][k]} ', transform=Axes[i][j].transAxes,
                    horizontalalignment=('right', 'left')[k], verticalalignment=('bottom', 'top')[k],
                    bbox=dict(boxstyle='round', fc=(1, 1, 1, 0.6), ec='lightgrey'), zorder=12)

# CONST
G = 6.674 * 10**-11 # Gravitational constant
R0 = 6371 * 10**3   # Radius of Earth
M0 = 5.974 * 10**24 # Mass of Earth

# VAR
m0 = 2 * 10**7      # kg
m1 = 2 * 10**5      # kg
alpha = 2 * 10**5   # kg/s
flow = 5000         # m/s
v = 0               # m/s
x = 0               # m
dt = 0.1            # s
k = 15 * (VAR=='k') # air

# FLIGHT
def launch(*, m0=m0, m1=m1, alpha=alpha, k=k, flow=flow, dt=dt, x=x, v=v, r=-1):
    EV = [0] * 5
    m, p, i = m0, m0*v, 0
    X, V, A, P, M, F = [x], [v], [], [p], [m], []
    while True:
        m -= alpha*dt
        if m < m1: break
        g = (G*M0)/(R0+x)**2
        p -= (alpha*(v-flow) + k*v**2 + m*g) * dt
        v = p / m
        x += v*dt
        i += 1

        for var in 'xvpm': exec(f'{var.upper()}.append({var})')

        assert x > 0
        if g*(R0+x) <= v**2:
            if not EV[0]:
                EV = [x, v, p, m, i*dt]
        else:
            assert not EV[0]

    T = [i*dt for i in range(i+1)]

    Lines.append([Axes[i//2][i%2].plot(T, (X, V, P, M)[i], zorder=O[r])[0] for i in range(4)])
    if EV[4]: [Axes[i//2][i%2].plot(EV[4], EV[i], '_r', zorder=11) for i in range(4)]

# RUN
if not ONCE:
    for i in range(10): launch(r=i, **{VAR: eval(f'{VAR}*BETA[i]')})
    fig.legend(title=f'${VARS[VAR]}=\\beta\\cdot {VARS[VAR]}$',
               handles=(L[0] for L in Lines),
               labels=(f'β = {c}' for c in BETA),
               ncol=5,
               loc='lower center')

launch();
for i in range(4): Lines[-1][i].set_color('black')

# OUT
# fig.savefig('tmp.png', dpi=225)
plt.show()
