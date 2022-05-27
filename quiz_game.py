print("Welcome to my game!")

# Ask the user if they want to play the game
playing = input("Do you want to play? ")

# Check if the user typed "yes" or "no" to decide whether to continue or end the program
if playing.lower() != "yes":
    quit()

print("Okay! let's play :)")

score = 0

# Question for the user 
answer = input("What is my codename? ")

# To check if the user's answer is correct
if answer.lower() == "blink":
    print("Correct!")
    score += 1
else:
    print("Oops! Wrong")

# Question 2
answer = input("Who is the CEO of Microsoft? ")

# Answer
if answer.lower() == "satya nadella":
    print("Correct!")
    score += 1
else:
    print("Oops! Wrong")

# Question 3
answer = input("Who is the founder of Oracle? ")

# Answer
if answer.lower() == "larry ellison":
    print("Correct!")
    score += 1
else:
    print("Oops! Wrong")

# Question 4
answer = input("What is 2 multiplied by the highest factor of 24? ")

# Answer
if answer == "24":
    print("Correct!")
    score += 1
else:
    print("Oops! Wrong")

# Question 5
answer = input("Who is the greatest footballer of all time? ")

# Answer
if answer.lower() == "cristiano ronaldo":
    print("Correct!")
    score += 1
else:
    print("Oops! Wrong")

# The user's final score
print("Your final score is " + str(score) + "/5. Thanks for playing!" )
