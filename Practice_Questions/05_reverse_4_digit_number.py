# Write a program that will reverse a four digit number.Also it checks whether the reverse is true.

original_num = int(input("Enter a four digit number : "))
temp = original_num
reverse_num = 0

while temp > 0:
    last_digit = temp % 10
    reverse_num = (reverse_num * 10) + last_digit
    temp //= 10

print(f"Original number => {original_num}")
print(f"Reverse number => {reverse_num}")

is_palindrome = (original_num == reverse_num)
print(f"Is it a palindrome? {is_palindrome}")


## Another way

original_num2 = input("Enter a for digit number : ")

reverse_num2 = original_num2[::-1]

print(f"Original number => {original_num2}")
print(f"Reverse number => {reverse_num2}")

is_palindrome2 = (original_num2 == reverse_num2)
print(f"Is it a palindrome? {is_palindrome2}")