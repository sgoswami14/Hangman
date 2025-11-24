
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

