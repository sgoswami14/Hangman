# Hangman
An interactive version of a classic word game, Hangman and another version with added hints, implemented in Python. To familiarize yourself with the rules, see http://en.wikipedia.org/wiki/Hangman_(game). 

## Structure
```
Hangman/
|-- functions.py  # Helper functions
|-- hints.py  # Additional hints for an updated version
|-- hangman.py   # Main game: basic version
|-- hangman_with_hints.py  # Main game: updated version with hints
|-- words.txt     # List of available words
|-- README.md    # Documentation
````
## Requirements
Python 3.7+

## Game description
1. Select a word at random from the list of available words, the secret word.
2. A fixed number of guesses is allowed.
3. Make one guess that
   a. If correct, reveals the letter. 
   b. If incorrect, the number of guesses left is reduced.
4. To win, guess the secret word before the allowed guesses are over.
5. If out of guesses, you lose, and the secret word is revealed.

## How to Run
1. Clone the repository
```bash
git clone https://github.com/sgoswami14/Hangman.git
cd Hangman
```
3. Run the basic version of the game
```bash
python hangman.py
```

OR

4. Run the version of the game with hints
```bash
python hangman_with_hints.py
```



