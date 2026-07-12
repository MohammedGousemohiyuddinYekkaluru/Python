# 41) Write a program to print the following pattern
#   *
#   * *
#   * * *
#   * * * *
#   * * * * *

num = 5

for i in range(1, num+1):
    for j in range(i):
        print("*", end=" ")
    
    print()
