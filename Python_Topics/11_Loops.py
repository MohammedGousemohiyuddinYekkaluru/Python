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

## for loop -> it is used when we know how many iterations are needed beforehand...

# range function
list(range(1, 11)) # [1 - 10] 11 is not included

list(range(5)) # [0, 1, 2, 3, 4]

list(range(1, 11, 3)) # step "3" [1, 4, 7, 10]

for i in range(1, 11):
    print(i)

for i in "Andhra":
    print(i)

for i in [1, 2, 3, 4]:
    print(i)

for i in (1, 2, 3, 4):
    print(i)