README

Run 'python3 main.py' in the terminal to get answer.

My solution for this problem is to compare all the cows with each other and figure out the # of times they meet with compare().
I originally tried to solve the problem with a for loop but then realized it would be easier and more efficiet to find the relative velocities b/w the two cows being compared. Also the for loop method didn't account for a runtime of 2.84s for example.

The cows meet once the distance b/w them increases to the length of the track. The distance inceases by the relative velocity. So:

Answer (Rounded Down) = (time_of_race * (Vy - Vx)) / length_of_track



Runtime should be around O(n^2) but it doesn't run compare() when y < x to avoid repeats and doesn't compare cows to themselves or other same speed cows.

The given example runs compare() 6 times instead of 16.

I've also added data2.txt to play around with more #'s and it looks right to me.