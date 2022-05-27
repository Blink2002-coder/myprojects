name = input("Type your name: ")
print("Welcome", name + ", to this adventure!")

answer = input("You have reached the end of the road. Turn left or right: ").lower()

if answer == "left":
    answer_2 = input("You've come to a river, you can walk around it or swim across it. Type 'walk' to walk around it and 'swim' to swim across it: ").lower()

    if answer_2 == "walk":
        print("You walked for many miles and ran out of water and energy. You lost the game!")
    elif answer_2 == "swim":
        print("You were eaten by a big shark.")
    else:
        print("Not a valid option. You lose!")

elif answer == "right" :
    answer_3 = input("You come to a bridge. Do you want to cross it or head back? Type 'cross' to cross and 'head back' to go back: ").lower()
    if answer_3 == "cross":
        print("You crossed the bridge to the other side and now you're safe. You win!")
    elif answer_3 == "head back":
        print("You would have won the game if you crossed the bridge. You lose!") 
    else:
        print("Invalid option. You lose!")

else:
    print("Not a valid option. You lose!")

print("Thank you for playing the game. It was fun. Goodbye!")
