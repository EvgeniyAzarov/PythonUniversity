import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

a = -4*np.pi
b = 4*np.pi
m = 10

x = np.linspace(a, b, int((b - a) * 50))

fig = plt.figure()
ax = plt.axes()
ax.set(xlim=(a,b), ylim=(-2, 2))

#ax.spines['top'].set_color('none')
#ax.spines['right'].set_color('none')

#ax.spines['bottom'].set_position(('data', 0))
#ax.spines['left'].set_position(('data', 0))

line, = ax.plot([], [], lw=2)


def cos_gen(x):
    s = np.ones_like(x)
    a = np.ones_like(x)
    
    i = 1
    while True:
       a *= -x**2 / ((2*i-1)*(2*i)) 
       s += a
       i += 1
       yield s
   
   
gen = None
def init():
    plt.plot(x, np.cos(x), "--r", lw=1)
    line.set_data([], [])
    
    global gen
    gen = cos_gen(x)
    
    return line, 


def animate(i):
   y = next(gen)
   line.set_data(x, y)
   return line,
   

anim = FuncAnimation(fig, animate, init_func=init, frames=m, interval=500, repeat=False)
plt.show()
anim.save("cos.gif", writer="pillow")

