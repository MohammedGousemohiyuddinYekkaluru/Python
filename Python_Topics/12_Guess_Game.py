# Guess The Correct number from 1 - 100

correct_num = 50

attempts = 0

guess_num = int(input("Guess a number from 1 - 100 : "))

while True:
    if guess_num == correct_num:
        attempts += 1
        print("Your guess is correct", f"you guessed in {attempts} attempts")
        break
    else:
        if guess_num > correct_num:
            attempts += 1
            print("Wrong guess, guess lower, Try again")
            guess_num = int(input("Guess a number from 1 - 100 : "))
        else:
            attempts += 1
            print("Wrong guess, guess higher, Try again")
            guess_num = int(input("Guess a number from 1 - 100 : "))
    