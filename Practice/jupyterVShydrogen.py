
# IMPORTS
%matplotlib inline
import numpy as np
import math, sys
from pylab import *
from tqdm import tqdm
import time
style.use('seaborn-whitegrid')
rcParams['figure.figsize'] = [15, 10]

""" O(n) """

def solutionN(number):
    sum_list=[]
    for x in range(number):
        if x%3==0 or x%5==0:
            sum_list.append(x)

    return sum(sum_list)

def solutionN2(number):
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)

""" O(1) """
def solution1(number):
    a3 = (number-1)//3
    a5 = (number-1)//5
    a15 = (number-1)//15
    result = (a3*(a3+1)//2)*3 + (a5*(a5+1)//2)*5 - (a15*(a15+1)//2)*15
    return result

trials = np.linspace(100, 1e5, 30)

time_O1=[]
time_ON=[]



for number in trials:
    start = time.time()
    solutionN2(int(number))
    end = time.time()
    time_ON.append(end-start)


    start = time.time()
    solution1(int(number))
    end = time.time()
    time_O1.append(end-start)


plot(trials, time_O1)
plot(trials, time_ON)
show()
