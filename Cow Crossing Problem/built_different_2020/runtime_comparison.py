import new

# IMPORTS
import numpy as np
import math, sys
from pylab import *
style.use('seaborn-whitegrid')
rcParams['figure.figsize'] = [20, 8]



nsquare_results=[]
nlogn_results=[]

test_cases=[]

for x in list_of_tests:




subplot(1, 3, 1)
title("phi = 5")
xlabel("Phi (0 - Pi)")
ylabel("Population Response")
plot(plot_range, c1, 'r', label='C=1')
plot(plot_range, c01, 'b', label='C=0.1')
legend(loc='upper right')
