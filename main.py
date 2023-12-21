#import matplotlib.pyplot as plt
import math

def conformity_area(r, a, b, t_0):

    ln = math.log(b * (1 - a)**-1)

    k = ((n * (r - 1)) / (t_0 * math.log(r))) 
    k_1 = ln / math.log(r)

    k_lower = str(k) + " t " + str(k_1) 
    return k_lower

def non_conformity_area(r, a, b, t_0):
    ln = math.log(a)

r = 1.5 # 1.5
a = 0.1 # 0.05
b = 0.1 # 0.05
n = 2 # 2
t_0 = 150 # 150
t_1 = 100 # 100
h_0 = 18.6 # 28.03
h_1 = 24.43 # 36.74

M_T0 = (h_0 * t_0) / n
M_T1 = (h_1 * t_1) / n

conformity = conformity_area(r, a, b, t_0)

non_conformity = non_conformity_area(r, a, b, t_0)



