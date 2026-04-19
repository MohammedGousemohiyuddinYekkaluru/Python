# User will input (3ages).Find the oldest one

age1 = int(input("Enter age 1 : "))
age2 = int(input("Enter age 2 : "))
age3 = int(input("Enter age 3 : "))

ages = [age1, age2, age3]

oldest_age = 0

for age in ages:
    if age > oldest_age:
        oldest_age = age

print(oldest_age)