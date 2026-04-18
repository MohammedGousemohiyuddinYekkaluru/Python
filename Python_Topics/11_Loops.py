# Loop => a loop is a control flow statement used to execute a specific block of code repeatedly as long as a certain condition is met.

## in python there are 2 types og loops
# while loop 
# for loop

## While loop -> it is used when you don't know how many iterations are needed beforehand (e.g., waiting for user input).

# Example => print a table of user input number

number = int(input("Enter a number"))

i = 1

while i < 11:
    print(number * i)
    i += 1