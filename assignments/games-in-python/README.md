
# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a text-based Hangman game in Python to practice string manipulation, loops, conditionals, user input, and random selection.

## 📝 Tasks

### 🛠️ Set Up the Game

#### Description

Use the provided list of words to randomly select a secret word and initialize the game state.

#### Requirements

Completed program should:

- Randomly select one word from the provided list.
- Create a collection to track the letters guessed by the player.
- Set a maximum number of incorrect guesses.

### 🛠️ Build the Game Loop

#### Description

Create the main game loop that displays the player's progress, accepts guesses, and updates the game state.

#### Requirements

Completed program should:

- Display the secret word as underscores for letters that have not been guessed.
- Accept a single-letter guess from the player.
- Track correct and incorrect guesses.
- Prevent a repeated guess from being counted more than once.

Example progress display for the word `python` after guessing `p` and `o`:

```text
p _ _ _ _ _
Incorrect guesses: o
```

### 🛠️ End the Game

#### Description

End the game when the player reveals the entire word or reaches the maximum number of incorrect guesses.

#### Requirements

Completed program should:

- Display a winning message when the player guesses the word.
- Display a losing message and reveal the secret word when the player runs out of guesses.
- Clearly show the number of incorrect guesses remaining while the game is in progress.
