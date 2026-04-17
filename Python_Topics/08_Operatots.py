# Operators are used to perform operaions on variable and values. Python has the following operators:

# Arithmetic operators
# Comparison operators
# Logical operators
# Bitwise operators
# Assigment operators
# Identity operators
# Membership operators

## Arithmetic operators
x = 5
y = 2

print(x + y) #7
print(x - y) #3
print(x * y) #10
print(x / y) #2.5
print(x % y) #1
print(x ** y) #25
print(x // y) #2 # integer division

## Comparision operators
print(x > y) 
print(x < y)
print(x >= y)
print(x <= y)
print(x == y)
print(x != y)

## Logical operators
x = True
y = False

print(x or y) # True
print(x and y) # False
print(not y) # True

## Bitwise operators
x = 2
y = 3

print(x & y) #2
print(x | y) #3
print(x >> 2) #right shift
print(x << 3) #left shift
print(~x)

## Assignment operator
a = 3  # "=" is an assignment operator
print(a)

a += 3 #a = a + 3
print(a)

## Identity operators => checks memory location
a = 3
b = 3

print(a is b) #True -> because of same memory loaction

a = "Hello"
b = "Hello"

print(a is b) #True

a = [1, 2, 3]
b = [1, 2, 3]

print(a is b) #False

## If two variables looks same that doesn't mean that they are stored in same memory location

## Membership operator
x = "Delhi"

print("D" not in x) #False

x = (1, 2, 3)
print(5 in x) #False