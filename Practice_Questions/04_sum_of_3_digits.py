# Write a program that will give you the sum of 3 digits

number = input("Enter a three digit number : ")

sum = 0

for i in number :
    sum += int(i)

print(sum)