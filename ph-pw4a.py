from matplotlib.animation import FuncAnimation
from matplotlib import pyplot as plt
import numpy as np


class Front(plt.Circle):

    def __init__(self, *args, r, dr, **kwargs):
        super().__init__(radius=r[0], *args, **kwargs)
        self.r = r[1]
        self.dr = dr

    def iter(self):
        self.radius += self.dr
        self._alpha = 1 - self.radius / self.r
        return self._alpha > 0


def get_front(pos):
    return Front(pos, r=(0, 2), dr=velocity['wave']*dt, fill=False)

def update(frame):
    position[0] += velocity['source'](frame*dt)*dt
    source.set_xdata(position[0])
    if not frame % 10:
        Fronts.append(get_front(position.copy()))
        ax.add_patch(Fronts[-1])
    for i, front in enumerate(Fronts):
        if not front.iter():
            front.remove()
            del Fronts[i]

fig = plt.figure(tight_layout=True)
ax = fig.subplots()
ax.set_axis_off()
ax.set_xlim(-2.2, 2.2)
ax.set_ylim(-1.64, 1.64)
ax.set_aspect('equal')

v, a = 2, 2
velocity = {'wave': 3, 'source': lambda t: v+a*t}
position = [-2, 0]
dt = 0.01

Fronts = []
frames = int(8/(v+(v**2+a*8)**.5)/dt)
source, = ax.plot(*position, 'o', c='r')
anim = FuncAnimation(fig, update, frames=frames, interval=20, repeat=0, init_func=lambda: ...)
plt.show()
