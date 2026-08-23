import random

number = random.randint(1, 10)

print("I have selected a number between 1 and 10.")

guess = int(input("Guess the number: "))

while guess != number:

    if guess < number:
        print("Too low!")
    else:
        print("Too high!")

    guess = int(input("Guess again: "))

print("🎉 Correct! You guessed the number!")
