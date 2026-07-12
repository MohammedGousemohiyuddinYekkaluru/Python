# 42) Write a program to print the following pattern
#  *
#  **
#  ***
#  **
#  *

num = 3

for i in range(1, num+1):
    for j in range(i):
        print("*", end=" ")
    
    print()

for k in range(num-1, 0, -1):
    for l in range(k):
        print("*", end=" ")
    
    print()
