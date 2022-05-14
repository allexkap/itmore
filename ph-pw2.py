from matplotlib.animation import FuncAnimation
from matplotlib import pyplot as plt
import numpy as np

dx, dt = 0.05, 0.1
A2 = 429/235/1049
CF = A2*dt/dx/dx
print(f'{CF = }')

X = np.arange(0, 8+dx, dx)
T = np.cos(X)/2
T[0], T[-1] = 0.5, 0.5

def step(): 
    T[1:-1] += CF*(T[2:]-2*T[1:-1]+T[:-2])

def update(frame):
    print(frame)
    if frame:
        for i in range(90): step()
        line.set_ydata(T)
        text.set_text(f'{frame*dt*90/60:.0f} min')
    return line, pt, text


fig = plt.figure(label='Thermal Conductivity', figsize=(6.4, 4.8), tight_layout=True)
ax = fig.subplots()
ax.set_title('T(x)')

ax.text(0.985, -0.055, 'x, m', transform=ax.transAxes, bbox=dict(boxstyle='round', fc=(1, 1, 1, 0.6), ec='lightgrey'))
ax.text(-0.05, 0.92, 'T, $^\circ$C', transform=ax.transAxes, bbox=dict(boxstyle='round', fc=(1, 1, 1, 0.6), ec='lightgrey'), rotation=90)
text = ax.text(1-0.02, 0.02, '0 min', transform=ax.transAxes, horizontalalignment='right', verticalalignment='bottom')

line, = ax.plot(X, T, '-', c='black')
pt, = ax.plot([0, 8], [0.5, 0.5], '8', c='red')
anim = FuncAnimation(fig, update, frames=401, blit=True, interval=20, repeat=0)
# anim.save('tmp.mp4', fps=50, dpi=225)
# fig.savefig('tmp.png', dpi=225)
# np.save('tmp.npy', T)
plt.show()
