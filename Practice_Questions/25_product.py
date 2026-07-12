# 25) Write a program that can multiply 2 numbers provided by the user without using the * operator

import math

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))

nums = [num1, num2]

result = math.prod(nums)
print(result)