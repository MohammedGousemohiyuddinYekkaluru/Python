# 26) Write a program that can find the factorial of a given number provided by the user.

num = int(input("Enter a number: "))

fact_res = 1

for i in range(num, 1, -1):
    fact_res *= i

print(fact_res)