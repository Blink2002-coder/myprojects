import random
from Dictionary import Words
import string

def get_valid_word(Words):
    word = random.choice(Words)   # Randomly chooses a word from dictionary list
    while '-' in word or ' ' in word:
        word = random.choice(Words)

    return word.upper()

def hangman():
    word = get_valid_word(Words)
    word_letters = set(word)  # Letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # Keeps track of what the user has guessed

    lives = 6

    # Getting user input
    while len(word_letters) > 0 and lives > 0:
        # Letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print("You have", lives, "lives left and you have used these letters: ", " ".join(used_letters))

        # what the current word is (i.e W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", " ".join(word_list))

        user_letter = input("Guess a letter: ").upper()
        
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            
            else:
                lives -= 1  # Takes away a life if wrong
                print("Letter is not in word")

        elif user_letter in used_letters:
            print("You have already used that character. Please try again!")

        else:
            print("Invalid character. Please try again")

    # Gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print("Sorry, you died! The word was", word)
    else:
        print("You guessed right!")

hangman()