name = input("Enter your name : ")

print(name)

# Lets do a task => ask user for two numbers and perform addition to it and print the result

first_num = input("Enter first number : ") #inputs gives strings # ex num1 = 3
second_num = input("Enter second number : ") # num2 = 3

result = first_num + second_num
print(result) # 33

# To avoid that we do type conversion
# lets do the same task

third_num = int(input("Enter third number : ")) # 3
fourth_num = int(input("Enter fourth number : ")) # 3

result2 = third_num + fourth_num
print(result2) # 3+3=6 

# String("") is a universal data type it can store any type of data type init..

# Type conversion => changing one data type to another data type
# There are two types of type conversion 1) implicit 2) explicit

# For Example :-
print(4 + 5.5) # we are adding one integer and one float data type
# the python interpreter implicitly converts the data type to the float...

# Explicit example
age = int(input("Enter your age : "))
print(age)
print(type(age))

# Convert the data type which is convertable, dont do like this int('Kolkata').. which is not possible.., and throws error...

# Point to remember :- Type conversion is not a permanent operation...
# means => it doesn't changes the original data type of the variable

# example:-

a = 4.5 # float

int(a) # 4 (integer)

print(a, type(a)) # 4.5, float