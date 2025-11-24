
import random
import string
import numpy as np

# Path to word list
WORDLIST_FILENAME = "words.txt"

def load_words():
    """Load a list of valid words in lowercase letters from file."""
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """ Choose a word from the wordlist at random."""
    return random.choice(wordlist)



# -------------------------------
# Helper Functions
# -------------------------------

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word to guess
    letters_guessed: letters have been guessed so far
    Return True if all letters in the secret word have been guessed.
    '''
    for l in secret_word:
      if l in letters_guessed:
        pass
      else:
        return False

    return True



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    Return the current guessed word with underscores for missing letters.
    '''
    st = ''
    for l in secret_word:
      if l in letters_guessed:
        st = st + l + ' '
      else:
        st = st + '_' + ' '
    return st

def get_available_letters(letters_guessed):
    '''
    letters_guessed: letters guessed so far
    Return a string of letters that have not been guessed.
    '''
    all_letters = string.ascii_lowercase
    req_st = ''.join([s for s in all_letters if s not in letters_guessed])
    return req_st

def lose_warning(n_warning, guesses_used, secret_word, letters_guessed):
"""Handle warning reduction or guess loss."""
  if n_warning > 0:
    n_warning = n_warning - 1
    guess = get_guessed_word(secret_word, letters_guessed)
  else:
    guesses_used = guesses_used + 1
    print("No more warning. Losing 1 guess")
  return n_warning, guesses_used


