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

# Instructor version

import random # random module for generating random numbers

jackpot = random.randint(1, 100) # both numbers are included

guess = int(input("guess the number : "))
counter = 1

while guess != jackpot:
    if guess < jackpot:
        print("Guess Higher")
    else:
        print("Guess Lower")
    
    guess = int(input("guess the number : "))
    counter += 1

print("Correct guess")
print("you took", counter, "attempts")
    