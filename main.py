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


plt.axis([0, 800, 0, 10])

t = np.linspace(0, 800) # Тут можно косарь поставить для наглядности, если это работает так как я дума.
x_t = np.linspace(0, 10)
k1 = conformity[0] * t + conformity[1]
k2 = non_conformity[0] * t + non_conformity[1]

plt.plot(t, k1, 'r', label = str(round(conformity[0], 4)) + ' * ' + 't ' + ' + ' + str(round(conformity[1], 4)))
plt.plot(t, k2, 'g', label = str(round(non_conformity[0], 4)) + ' * ' + 't ' + ' + ' + str(round(non_conformity[1], 4)))
#plt.plot(t, x_t)   # это то что является ступеньчатим на том графике
plt.grid(True)
plt.xlabel('t')
plt.ylabel('X(t)')
plt.legend()
plt.show()
