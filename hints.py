
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
