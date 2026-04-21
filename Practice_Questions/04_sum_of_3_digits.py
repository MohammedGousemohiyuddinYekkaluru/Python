# Write a program that will give you the sum of 3 digits

number_1 = input("Enter a three digit number : ")

sum = 0

for i in number_1 :
    sum += int(i)

print(sum)

# Another way
number = int(input("Enter a three digit number : "))

digit_3 = number % 10   #gets the last digit and stores in digit_3
number = number // 10   # removes the last digit, just 2 digits remains

digit_2 = number % 10
digit_1 = number // 10

result = digit_1 + digit_2 + digit_3

print(result)