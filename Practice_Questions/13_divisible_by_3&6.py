# 13 - Write  a program that will tell whether the given number is divisible by 3 & 6.

number = int(input("Enter a number : "))

if number % 3 == 0 and number % 6 == 0:
    print("given number {} is divisible by 3 & 6".format(number))

else:
    print("given number {} is not divisible by 3 & 6".format(number))