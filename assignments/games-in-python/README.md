# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build the classic Hangman word-guessing game in Python while practicing string manipulation, loops, conditionals, and random selection.

## 📝 Tasks

### 🛠️ Select a Random Secret Word

#### Description
Create a predefined list of words and have the program randomly choose one of them as the secret word at the start of each game.

#### Requirements
Completed program should:

- Store at least 5 words in a predefined list
- Use the `random` module to select one word per game
- Hide the selected word from the player

### 🛠️ Accept Guesses and Show Progress

#### Description
Prompt the player to guess one letter at a time and display the current state of the word, revealing correctly guessed letters.

#### Requirements
Completed program should:

- Accept a single letter guess from the user on each turn
- Display progress using underscores for unrevealed letters (e.g., `_ a _ _ m a _`)
- Ignore or warn about letters that have already been guessed

### 🛠️ Track Attempts and End the Game

#### Description
Keep track of incorrect guesses and end the game when the player either reveals the whole word or runs out of attempts.

#### Requirements
Completed program should:

- Track and display the number of incorrect guesses remaining
- End the game when the word is fully guessed or attempts are exhausted
- Display a clear win or lose message, revealing the word if the player loses

```
Word: _ y _ _ o _
Attempts remaining: 4
Guess a letter: p
Word: p y _ _ o _
```
