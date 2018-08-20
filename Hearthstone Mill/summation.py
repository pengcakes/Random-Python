import sys

#run = True
while True:
    sumx = 0
    var = input("Enter x: ")
    var2 = input("Enter y: ")
    
    
    if type(var) == int:
            for i in range(var, var2 + 1):
                sumx = sumx + i
            print ("Answer: " + str(sumx) + "\n")
        
    else:
        print("invalid")
        
        
    
