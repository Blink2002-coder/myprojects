# A game of rock, paper, scissors between the computer and the user
import random

# To keep track of how many wins the user and computer have had while playing the game
user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]


while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break    # To break out of the while loop

    if user_input not in options:
        continue    # To continue to start from the beginning of the loop until the user types rock, paper or scissors

    random_number = random.randint(0, 2) 
    # rock: 0, paper: 1, scissors: 2

    computer_pick = options[random_number]          # What the computer will pick
    print("Computer picked " + computer_pick + ".")

# To determine who wins each round
    if user_input == "rock" and computer_pick == "scissors":
        print("You win!")
        user_wins += 1
    
    elif user_input == "paper" and computer_pick == "rock":
        print("You win!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You win!")
        user_wins += 1
        
    elif user_input == computer_pick:
        print("Tie")
        user_wins += 0
        computer_wins += 0

    else:
        print("You lose!")
        computer_wins += 1


# To see who won the game by how many or whether it ended in a tie
if user_wins > computer_wins:
    print("You won the computer " + str(user_wins) + "-" + str(computer_wins) + ".")
elif user_wins == computer_wins:
    print("You drew with the computer " + str(user_wins) + "-" + str(computer_wins) + ".")
else:
    print("The computer won " + str(computer_wins) + "-" + str(user_wins) + ".")

print("Goodbye!")    
