import raybeam_questions, time

# IMPORTS
import numpy as np
import math, sys
from pylab import *
style.use('seaborn-whitegrid')
rcParams['figure.figsize'] = [20, 8]


tests=[10, 1000, 10000, 100000, 1000000, 10000000, 1000000000]
runtime_results_1, runtime_results_2=[],[]

for cases in tests:
    #read file into list
    sTime = time.time()

    raybeam_questions.find_all_factors_0(cases)
    run_time =  round( (time.time() - sTime), 8)

    runtime_results_1.append(run_time)

for cases in tests:
    #read file into list
    sTime = time.time()

    raybeam_questions.find_all_factors_1(cases)
    run_time =  round( (time.time() - sTime), 8)

    runtime_results_2.append(run_time)



title("Runtime Comparison")
xlabel("Increasingly large test cases.")
ylabel("Runtime")
plot(tests, runtime_results_1, 'r', label='n')
plot(tests, runtime_results_2, 'b', label='1/4n')
legend(loc='upper right')

show()
