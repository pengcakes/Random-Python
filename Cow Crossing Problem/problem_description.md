PROBLEM NAME: running INPUT FORMAT:

* Line 1: Three space-separated integers: N, L, and C. (1 <= L,C <= 25,000).

* Lines 2..1+N: Line i+1 contains the speed of cow i, an integer in the range 1..1,000,000.

 

SAMPLE INPUT (file running.in):

4 2 100

20

100

70

1

INPUT DETAILS: There are 4 cows running 2 laps on a circular track of length 100. The speeds of the cows are 20, 100, 70, and 1.

 

OUTPUT FORMAT: * Line 1: The total number of crossing events during the entire race.





20 100
2 

20 70
1 

70 100
0 

1 20
0 

1 100
2 

1 70
1 
