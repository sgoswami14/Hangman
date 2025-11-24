import random
import numpy as np


from functions import is_word_guessed, get_available_letters, get_guessed_word, lose_warning
from hints import match_with_gaps, show_possible_matches


# -------------------------------
# Hints for the Game 
# -------------------------------

def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    '''

    my_chrs = [l for l in list(my_word) if l != ' ']

    if len(my_chrs) == len(other_word):
        matches = [i for i in range(len(my_chrs)) if my_chrs[i] == list(other_word)[i] or my_chrs[i] == '_']
        if len(my_chrs) == len(matches):
            return True
    else:
        return False

def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''

    print("\nShowing possible matching words.")
    print("")

    all_matches = [other_word for other_word in wordlist if match_with_gaps(my_word, other_word)]

    req_word = ''.join([l for l in list(my_word) if l != ' '])
    # missing letter positions
    missing_index = [i for i, chr in enumerate(list(req_word)) if chr == '_']

    all_posible_match = []
    for i, word in enumerate(all_matches):
        missing_letters = np.array(list(word))[missing_index]
        if set(missing_letters).isdisjoint(set(list(req_word))):
            print(word)
            all_posible_match.append(word)



############################################



def hangman_with_hints(secret_word, nguess=6, n_warning=3):
    '''Starts up an interactive game of Hangman with possible hints.'''

    print("\nWelcome to the game Hangman with hints!!")
    print(f"The secret word contains", len(secret_word), "letters.")
    print("Number of guesses allowed", nguess)
    print("Number of warnings", n_warning)
    print("------------------------------------------------------")


    letters_guessed = []
    i = 1

    while i <= nguess:
        print(i, nguess)

        if is_word_guessed(secret_word, letters_guessed):
            #Total score = guesses_remaining* number unique letters in secret_word
            guess_left = nguess-i+1
            n_unique = np.unique(np.array(list(secret_word)))
            score = guess_left * len(n_unique)
            print("Congratulations, you won!")
            print("Your final score is", score)
            break

        # Print number of guesses and available letters.
        print("\nYou have", nguess-i+1, "guesses left.\n")
        available_letters = get_available_letters(letters_guessed)
        print("The available letters are: ", available_letters)

        # Guess letter
        l_guess = input("Guess a letter:")

        # Check if input is an alphabet.
        if str.isalpha(l_guess):
            # Make sure the letter is lowercase.
            l_guess = str.lower(l_guess)
            # Check if already guessed same letter.
            if l_guess in letters_guessed:
                n_warning, i = lose_warning(n_warning, i)
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
                    # Check if vowel.
                    if l_guess in vowels:
                      i = i+2
                    # If constant.
                    elif l_guess in consonants:
                        i = i+1
                    guess = get_guessed_word(secret_word, letters_guessed)
                    print("Oops! Letter not in secret word. Try again.", guess)
                    print("-----------------------------------")


        # Hints: Show possible matching words.
        elif l_guess == '*':
            print("Asked for hints.")
            show_possible_matches(guess)

        else:
            # If not alphabet or '*' warning reduces by 1.
            n_warning,i = lose_warning(n_warning, i)
            print("Invalid input. Enter only alphabets.", n_warning, "warnings left:", guess)
            print("-----------------------------------")

        if i > nguess:
            print("\nSorry, you lost the game.")
            print("The secret word is", secret_word)

    pass


# -------------------------------
# Play Game
# -------------------------------

if __name__ == "__main__":
    wordlist = load_words()
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)


