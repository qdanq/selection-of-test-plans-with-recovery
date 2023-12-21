import matplotlib.pyplot as plt
import numpy as np
import math

def conformity_area():

    ln = math.log(b * (1 - a)**-1)

    k = ((n * (r - 1)) / (t_0 * math.log(r))) 
    k1 = ln / math.log(r)

    return [k, k1]

def non_conformity_area():
    A = 2.062 
    k = (n * (r - 1)) / (t_0 * math.log(r))
    k1 = A / math.log(r)
    return [k, k1]

r = 1.5 # 1.5
a = 0.05 # 0.05
b = 0.05 # 0.05
n = 2 # 2
t_0 = 150 # 150
t_1 = 100 # 100
h_0 = 28.03 # 28.03
h_1 = 36.74 # 36.74

M_T0 = (h_0 * t_0) / n
M_T1 = (h_1 * t_1) / n

conformity = conformity_area()
non_conformity = non_conformity_area()


plt.figure

plt.axis([0, 800, 0, 10])

t = np.linspace(0, 800)
y1 = conformity[0] * t + conformity[1]
y2 = non_conformity[0] * t + non_conformity[1]

plt.plot(t, y1)
plt.plot(t, y2)
plt.grid(True)
plt.xlabel('t')
plt.ylabel('X(t)')
plt.legend()

plt.style.use('_mpl-gallery')
x_t = np.linspace(0, 10)

fig, ax = plt.subplots()

ax.stairs(x_t, linewidth=2.5)

ax.set(xlim=(0, 800), xticks=np.arange(0, 80),
       ylim=(0, 10), yticks=np.arange(0, 10))

plt.show()

