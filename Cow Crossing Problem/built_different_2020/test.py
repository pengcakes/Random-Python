# def oneplus(x):
#     return x+1
#
#
# def whytho(func):
#     return func(9)
#
#
# cond1 = True and False
#
# print(cond1)
#
# print(whytho(oneplus))



# IMPORTS
import numpy as np
import math, sys
from pylab import *
style.use('seaborn-whitegrid')
rcParams['figure.figsize'] = [20, 8]

#1
n=100
k=1
f_max=20
f0=5

# method for pop. response f(c, phi)
# THIS FUNCTION TAKES phi_I AS INPUT TO GENERATE VALUES FOR A SET phi OVER 0 TO PI
def population_response(c, phi_I):
    response = f0 + c* f_max * math.exp(k *( math.cos(2*(math.radians(phi) - phi_I)) - 1) )
    return response

# range
plot_range = np.linspace(0, math.pi, n)

# find responses for c values at phi=-5
phi = 5
c1 = []
c01 = []
for x in plot_range:
    c1.append(population_response(1, x))

for x in plot_range:
    c01.append(population_response(0.1, x))

subplot(1, 3, 1)
title("phi = 5")
xlabel("Phi (0 - Pi)")
ylabel("Population Response")
plot(plot_range, c1, 'r', label='C=1')
plot(plot_range, c01, 'b', label='C=0.1')
legend(loc='upper right')


# find responses for c values at phi=5
phi = 5
phi_5 = []
phi_neg5 = []
for x in plot_range:
    phi_5.append(population_response(1, x))

phi=-5
for x in plot_range:
    phi_neg5.append(population_response(1, x))


subplot(1, 3, 2)
title("C=1")
xlabel("Phi (0 - Pi)")
ylabel("Population Response")
plot(plot_range, phi_5, 'r', label='Phi=5 degrees')
plot(plot_range, phi_neg5, 'b', label='Phi=-5 degrees')
legend(loc='upper right')


# find responses for c values at phi=10
phi = 10
phi_10 = []
phi_neg10 = []
for x in plot_range:
    phi_10.append(population_response(1, x))

phi=-10
for x in plot_range:
    phi_neg10.append(population_response(1, x))

subplot(1, 3, 3)
title("C=1")
xlabel("Phi (0 - Pi)")
ylabel("Population Response")
plot(plot_range, phi_10, 'r', label='Phi=10 degrees')
plot(plot_range, phi_neg10, 'b', label='Phi=-10 degrees')
legend(loc='upper right')


show()
