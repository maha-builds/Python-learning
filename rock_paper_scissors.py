game = ["stone", "paper", "scissors"]

import random

computer_chose = random.choice(game)
print("Random computer chose:", computer_chose)

user_chose = input("Enter your guess: ")
print("User guess is:", user_chose)

if computer_chose == user_chose:
    print("Draw")

elif computer_chose == "scissors" and user_chose == "paper":
    print("Computer win")

elif computer_chose == "scissors" and user_chose == "stone":
    print("User win")

elif computer_chose == "stone" and user_chose == "paper":
    print("User win")

else:
    print("Computer win")
