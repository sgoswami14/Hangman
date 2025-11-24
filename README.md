# Hangman
An interactive version of a classic word game, Hangman, implemented in Python. To familiarize yourself with the rules, see http://en.wikipedia.org/wiki/Hangman_(game).

## Structure
```
Hangman/
|-- hangman.py   # Main game
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
3. Run the game
```bash
python hangman.py
```



