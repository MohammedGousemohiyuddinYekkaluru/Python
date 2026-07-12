# 27) Write a program to print the first 25 odd numbers.

count = 0

for i in range(1, 100):
    if i % 2 != 0:
        print(i)
        count += 1
    
    if count == 25:
        break