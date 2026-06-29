# 20 - Write a program that will give you the in hand salary after deduction of HRA(10%),DA(5%),PF(3%), and tax(if salary is between 5-10 lakh–10%),(11-20lakh–20%),(20< _   – 30%)(0-1lakh print k).


CTC_amount = int(input("Enter your CTC : "))

in_hand_salary = CTC_amount - (CTC_amount * 0.1) - (CTC_amount * 0.05) - (CTC_amount * 0.03)

if CTC_amount > 2000000:
    in_hand_salary -= (in_hand_salary * 0.3)

elif CTC_amount > 1000000:
    in_hand_salary -= (in_hand_salary * 0.2)

elif CTC_amount > 500000:
    in_hand_salary -= (in_hand_salary * 0.1)

print(f"After all deductions your in hand salary is {in_hand_salary}")