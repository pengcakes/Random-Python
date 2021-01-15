"""
Austin New n log n

"""
import time
sTime = time.time()
#read file into list
file = 'data4.txt'
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

def compare(time_of_race, xrate, yrate, course_length):
	meet = 0
	relative_vel = yrate - xrate
	answer = (time_of_race * relative_vel) // course_length #round down

	#print("totalDistance", time_of_race * relative_vel)

	return answer

# O(n^2)
def main():
	crossing_events = 0
	#Y MUST BE BIGGER THAN X
	for x in data:
		for y in data:
			if (y != x and y > x):#avoid repeats and self comparisons
				#print('x:',x,'y:', y)
				#print('meets:',compare(time_of_race, x, y, course_length), '\n')
				crossing_events += compare(time_of_race, x, y, course_length)
	return crossing_events

# O(nlogn)	598964
def main2():
    data.sort()
    data.reverse()
    crossing_events = 0

    # problem is that it still iterates through the whole list anyways so still n^2
    #Y MUST BE BIGGER THAN X
    # iterates an extra time but saves time overall
    for x in data:
        for y in [i for i in data if i>x]:
            crossing_events += compare(time_of_race, x, y, course_length)

    return crossing_events


if __name__ == "__main__":
    print("\n\n")
    print('Total meets:', main2())
    run_time =  round( (time.time() - sTime), 8)
    print("--- %s seconds ---" % run_time)
    print("\n\n")
