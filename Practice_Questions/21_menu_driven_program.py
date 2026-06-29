# 21 - Write a menu driven program - 1.cm to ft  2.kl to miles  3.usd to inr  4.exit


print("1. cm to ft, 2. km to miles, 3. USD to INR, 4. exit")

while True:
    user_choice = input("choose one option from above : ")

    if user_choice == "1":
        cm = int(input("Enter the cm(centimeter) : "))

        ft = cm / 30.48
        print(f"{cm}cm in feet is {ft} feet")

    elif user_choice == "2":
        km = int(input("Enter the km(kilometer) : "))

        miles = km * 0.621371
        print(f"{km}km in miles is {miles} miles")

    elif user_choice == "3":
        USD = int(input("Enter the amount in dollars : "))

        INR = USD * 95
        print(f"{USD}$ in rupees is {INR} Rupees")

    elif user_choice == "4":
        break

    else:
        print("Choose the correct option")