# Write a program that will tell whether the given year is a leap year or not.

year = int(input("Enter a year : "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
             print(f"{year} is a Leap year")
        else:
            print(f"{year} is not a Leap year")
    else:
        print(f"{year} is a Leap year")
else:
    print(f"{year} is not a Leap year")


# Another way
# A year is a leap year if:
# 1. It is divisible by 4 AND (NOT divisible by 100 OR divisible by 400)

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a Leap year")
else:
    print(f"{year} is not a Leap year")