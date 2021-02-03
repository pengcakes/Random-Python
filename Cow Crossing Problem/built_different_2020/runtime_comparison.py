import new_test, time

# IMPORTS
import numpy as np
import math, sys
from pylab import *
style.use('seaborn-whitegrid')
rcParams['figure.figsize'] = [20, 8]



"""
BETTER WAY TO DO THIS
"""

tests=['data.txt', 'data2.txt', 'data3.txt','data4.txt']
runtime_results_1, runtime_results_2=[],[]

for cases in tests:
    #read file into list
    file = cases
    with open(file) as f:
    	data = f.read().split()
    data = [int(x) for x in data]

    num_of_cows = data[0] #N - Unused btw
    num_of_laps = data[1] #L
    course_length = data[2] #C

    total_distance = num_of_laps*course_length
    del data[0], data[0], data[0] #remove first 3

    time_of_race = total_distance / max(data) #race ends
    time_of_race = round(time_of_race, 2) #round to 2 places
    #determines how many times y meets x
    #relative velocity
    sTime = time.time()
    print(time_of_race)
    print('Total meets:', new_test.main2(data, time_of_race, course_length))
    run_time =  round( (time.time() - sTime), 8)
    print("--- %s seconds ---" % run_time)
    print("\n\n")

    runtime_results_1.append(run_time)

for cases in tests:
    #read file into list
    file = cases
    with open(file) as f:
    	data = f.read().split()
    data = [int(x) for x in data]

    num_of_cows = data[0] #N - Unused btw
    num_of_laps = data[1] #L
    course_length = data[2] #C

    total_distance = num_of_laps*course_length
    del data[0], data[0], data[0] #remove first 3

    time_of_race = total_distance / max(data) #race ends
    time_of_race = round(time_of_race, 2) #round to 2 places
    #determines how many times y meets x
    #relative velocity
    sTime = time.time()
    print('Total meets:', new_test.main(data, time_of_race, course_length))
    run_time =  round( (time.time() - sTime), 8)
    print("--- %s seconds ---" % run_time)
    print("\n\n")

    runtime_results_2.append(run_time)


title("Runtime Comparison")
xlabel("Increasingly large test cases.")
ylabel("Runtime")
plot(range(0,4), runtime_results_1, 'r', label='nlogn')
plot(tests, runtime_results_2, 'b', label='n^2')
legend(loc='upper right')

show()
