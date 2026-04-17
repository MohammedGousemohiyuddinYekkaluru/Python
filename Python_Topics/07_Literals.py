# Literals is a raw data in a variable. In python, there are various types of literals they are as follows:
# 1) Numeric literals
# 2) String literals
# 3) Boolean literals
# 4) Special literals

## 1) Numeric literal
a = 0b1010 # Binary literals
b = 100 # Decimal literal
c = 0o310 # Octal literal
d = 0x12c # Hexadecimal literal

#Float Literal
float_1 = 10.5
float_2 = 1.5e2
float_3 = 1.5e-3

#Complex literal
x = 3.14j

print(a, b, c, d)
print(float_1, float_2, float_3)
print(x, x.imag, x.real)

## 2) String literals

string = 'This is python'
strings = "This is python"
char = "c"
multiline_str = """This is a multiline with more than one line code."""
unicode = u"\U0001f600\U0001F606\U0001F923"
raw_str = r"raw \n string"

print(string)
print(strings)
print(char)
print(multiline_str)
print(unicode)
print(raw_str)

## 3) Boolean literal

a = True + 4 # 1 + 4 = 5
b = False + 10 # 0 + 10 = 10

print("a:", a)
print("b:", b)

## 4) Special literal
# safest way of variable declaration
a = None
print(a)