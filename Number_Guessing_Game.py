# This program generates a random number and finds out how many times it takes the user to guess the number

import random

# Tell the user to indicate the highest possible number to be generated by the Computer.
top_of_range = input("Type the highest possible number you want the computer to pick: ")

# To make sure the user typed a number and that the number is greater than zero
if top_of_range.isdigit():
    top_of_range = int(top_of_range)    # To convert what the user inputs to a number

    if top_of_range <= 0:
        print("Please type a number greater than zero next time.")
        quit()

else:
    print("Please type a number next time!")
    quit()

random_number = random.randint(0, top_of_range)


guess = ""

# To keep track of how many times the user has guessed
guess_count = 0

# This is where the game actually runs.
while guess != random_number:
    guess_count += 1
    guess = int(input("Guess the number the computer has picked: "))
    
    if guess < (random_number - 5):
        print("Your guess is too low! Try Again.")
    elif guess < random_number :
        print("Your guess is lower than the number! Try Again")

    elif guess > (random_number + 5):
        print("Your guess is too high! Try Again.")
    else:
         print("Your guess is higher than the number! Try again.")
print ("Correct! You got it in", guess_count, "guesses.")
