import random
import string
import numpy as np

from functions import load_words, choose_words
from functions import get_available_letters, lose_warning, get_guessed_word, is_word_guessed

# Path to word list
WORDLIST_FILENAME = "words.txt"
    
def hangman(secret_word, nguess=6, n_warning=3):
    """Start an interactive game of Hangman."""
    print("\nWelcome to the game Hangman!!")
    print(f"The secret word contains", len(secret_word), "letters.")
    print("Number of guesses allowed", nguess)
    print("Number of warnings", n_warning)
    print("------------------------------------------------------")

    letters_guessed = []
    guesses_used = 1

    while guesses_used <= nguess:
        print(guesses_used, nguess)

        # Print number of guesses and available letters.
        print(f"\nYou have {nguess-guesses_used+1} guesses left.\n")
        available_letters = get_available_letters(letters_guessed)
        print("The available letters are: ", available_letters)


        l_guess = input("Guess a letter:")
        
        if str.isalpha(l_guess):
            # Make sure the letter is lowercase.
            l_guess = str.lower(l_guess)
            # Check if already guessed the same letter. Lose warning if already guessed until warnings last then lose a guess.
            if l_guess in letters_guessed:
                n_warning, guesses_used = lose_warning(n_warning, guesses_used, secret_word, letters_guessed)
                print(l_guess, "already guessed before.", n_warning, "warnings left:")
                print("-----------------------------------")
            else:
                letters_guessed.append(l_guess)
                # Check if letter guessed is in secret word.
                if l_guess in secret_word:
                    guess = get_guessed_word(secret_word, letters_guessed)
                    print("Good guess:", guess)
                    print("-----------------------------------")
                # For letter guessed not in secret word.
                else:
                    all_letters = string.ascii_lowercase
                    vowels = ['a', 'e', 'i', 'o', 'u']
                    consonants = [i for i in all_letters if i not in vowels]
                    # If a vowel lose two guesses.
                    if l_guess in vowels:
                        guesses_used = guesses_used+2
                    # If consonant lose only one guess.
                    elif l_guess in consonants:
                        guesses_used = guesses_used+1
                    guess = get_guessed_word(secret_word, letters_guessed)
                    print("Oops! Letter not in secret word. Try again.", guess)
                    print("-----------------------------------")

        # If not alphabet warning reduces by 1 until available and then lose a guess.
        else:
            n_warning,guesses_used = lose_warning(n_warning, guesses_used, secret_word, letters_guessed)
            print("Invalid input. Enter only alphabets.", n_warning, "warnings left:", guess)
            print("-----------------------------------")


        #Check if the word is guessed:
        if is_word_guessed(secret_word, letters_guessed):
            #Total score = guesses_remaining* number unique letters in secret_word
            guess_left = nguess-guesses_used+1
            n_unique = np.unique(np.array(list(secret_word)))
            score = guess_left * len(n_unique)
            print("Congratulations, you won!")
            print("Your final score is", score)
            break


    # If all nguesses are over and word not yet correctly guessed, the game is lost.
    if guesses_used > nguess:
        print("\nSorry, you lost the game.")
        print("The secret word is", secret_word)

    pass

# -------------------------------
# Main Execution
# -------------------------------

if __name__ == "__main__":
    wordlist = load_words()
    secret_word = choose_word(wordlist)
    hangman(secret_word)
