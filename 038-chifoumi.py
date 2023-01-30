# a basic game of rock, paper, scissors
import random

while True:
    choices = ["rock","paper","scissors"]

    computer = random.choice(choices)
    player = None

    # keep asking the player till he picks something in the choices list
    while player not in choices:
        player = input("rock, paper, or scissors? ").lower()

    print("computer: ",computer)

    if player == computer: 
        print("Tie!")
    elif player == "rock":
        if computer == "paper":
            print("Computer wins!")
        else:
            print("You win!")
    elif player == "paper":
        if computer == "scissors":
            print("Computer wins!")
        else:
            print("You win!")
    else:
        if computer == "rock":
            print("Computer wins!")
        else:
            print("You win!")

    play_again = input("Play again?(yes/no) ").lower()
    
    if play_again != "yes":
        break

print("Goodbye!")