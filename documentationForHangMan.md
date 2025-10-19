# Fruit Hangman – Technical Documentation

## Overview
This program is a command-line fruit name guessing game. The game randomly selects a fruit, and the user guesses one letter at a time. The user has 3 lives; each incorrect letter reduces a life. The game ends when the word is fully guessed or when lives reach zero. The user is first asked for consent to play.

## How It Works (Flow)
1. `controller()` prints rules and prepares the fruit list.
2. `controller()` asks for consent via `get_consent()`.
3. If consent is `'y'`, `game(fruitList)` starts.
4. `game(...)`:
   - Picks a random fruit.
   - Creates an underscore list as blanks for each letter.
   - Loops while lives > 0 and the word is not fully revealed:
     - Takes a single-letter input.
     - Reveals all matching positions if correct; otherwise, decrements a life.
     - Ends early if the blanks match the chosen word.

## Functions

### `get_consent()`
- Prompts until the user enters `'y'` or `'n'` (case-insensitive, trimmed).
- Returns `'y'` or `'n'`.

```9:18:C:\Users\sonuh\code\shaurya\python\BasicPython\HangMan\HangMan.py
def get_consent():
    consent = input("Do you want to play the fruit guessing game type 'y' for yes and 'n' type no ")
    consent = consent.strip()
    consent = consent.lower()
    while consent != 'y' and consent != 'n':
        print("invalid input , try again ")
        consent = input("do you want to play the fruit guessing game for yes type 'y' for no type 'n' ")
        consent = consent.strip()
        consent = consent.lower()
    return consent
```

### `game(fruitList)`
- Chooses a random fruit; initializes `lives = 3`; tracks correct letters in a list of underscores.
- On each guess:
  - If the letter appears, reveals all its indices.
  - Else, decrements lives and prints feedback.
  - Success is detected when the joined blanks equal the chosen fruit.

```20:46:C:\Users\sonuh\code\shaurya\python\BasicPython\HangMan\HangMan.py
def game(fruitList):
    # randomly choosing a fruit
    i= random.randint(0,len(fruitList)-1)
    fruitChosenByAlgorithm = fruitList[i]
    print(fruitChosenByAlgorithm) # delete later 
    # right now the guessed word is empty
    blanksForInputs = ["_"] * len(fruitChosenByAlgorithm)
    # the user guessing the letter that goes in the blanks
    lives = 3
    print(blanksForInputs)
    while lives > 0 and "_" in blanksForInputs:
        userGuessLetter = input("Enter a letter that might be in the fruit: ")
        
        if userGuessLetter in fruitChosenByAlgorithm:
            for index, letter in enumerate(fruitChosenByAlgorithm) :
                if letter == userGuessLetter:
                    blanksForInputs[index] = userGuessLetter
            print("You are on the right track")
            print(blanksForInputs)
        else:
            print("Your input was wrong, make sure the letter is in the fruit picked by the function and input one at a time")
            print("You lost a life")
            lives = lives -1
        
        if "".join(blanksForInputs) == fruitChosenByAlgorithm:
            print("Success! You guessed the fruit:", fruitChosenByAlgorithm)
            break
```

### `rules()`
- Prints rules and returns a predefined fruit list.

```52:61:C:\Users\sonuh\code\shaurya\python\BasicPython\HangMan\HangMan.py
def rules():
    fruitList = ["apple","orange","kiwi","mango","pineapple"]
    print("------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("Welcome to the fruit guessing game")
    print(f"From the list of fruit [{fruitList}] you have to guess a randomly selected fruit")
    print("You will enter a letter at a time and get three live")
    print("If you get a letter wrong you will lose a life")
    print("Anytime you want to exit the game entre the symbol '*' the game ends ")
    print("------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    return fruitList
```

### `controller()`
- Orchestrates the flow.
- Always called at import/run time due to the last line.

```63:69:C:\Users\sonuh\code\shaurya\python\BasicPython\HangMan\HangMan.py
def controller():
    fruitList=rules()
    if get_consent() == 'y':
        game(fruitList)
    else:
        print("Have a good day. Lets play next time")
controller()
```

## Inputs and Outputs
- Input: From stdin
  - Consent: `'y'` or `'n'` (anything else loops).
  - Guesses: a string; code expects single letters but does not enforce it.
- Output: Printed messages, progress of guessed word as a list of characters.

## Game Rules (As Implemented)
- Lives: 3.
- Random fruit from `["apple","orange","kiwi","mango","pineapple"]`.
- Reveal every occurrence of a correctly guessed letter.
- End when:
  - The word is fully guessed, or
  - Lives reach zero.

Note: The rules mention entering `'*'` to exit, but that is not implemented in `game(...)`.

## Performance Characteristics
- Time per guess: O(n) where n = length of the fruit (scan and replace).
- Space: O(n) for the blanks list.
- I/O-bound with negligible CPU cost; random selection is O(1).

## Known Limitations / Observations
- Debug print exposes the chosen fruit (guarantees player can see the answer):
  - See `print(fruitChosenByAlgorithm)  # delete later`.
- No explicit handling for `'*'` to exit despite rules mentioning it.
- No input validation to enforce a single alphabetic character.
- Case sensitivity: guesses must match the case of the fruit list (all lowercase currently).
- Repeated correct guesses are allowed and harmless; repeated wrong guesses still cost a life each time.
- The guessed state is printed as a Python list (e.g., `['_', 'a', '_']`), not as a user-friendly string.

## How to Run
- Requirements: Python 3.x, standard library only.
- Run:
  - Windows PowerShell:
    ```powershell
    python .\HangMan.py
    ```

## Changes That Will Break Workflow or Logic
- Removing the return from `rules()` or changing its return type (must return a list of lowercase fruit strings).
- Not calling `controller()` (the game would never start when the file runs).
- Changing `while lives > 0 and "_" in blanksForInputs:` to something that doesn’t stop on win or life exhaustion.
- Removing or altering the `if "".join(blanksForInputs) == fruitChosenByAlgorithm:` success condition.
- Modifying `blanksForInputs` to a different length or type than the chosen fruit (must align index-by-index).
- Changing `enumerate(fruitChosenByAlgorithm)` replacement logic so it doesn’t update all matching indices.
- Altering `lives` initialization or decrement path so lives don’t reduce on wrong guesses.
- Changing `get_consent()` so it can return values other than `'y'`/`'n'` without updating `controller()`.
- Changing fruit list casing without normalizing user input (would break membership checks).
- Removing `random` selection (or providing an empty fruit list) causing index errors on `randint`.
- Replacing the list of underscores with a string without updating all index assignments.
- Deleting or keeping `print(fruitChosenByAlgorithm)` unintentionally:
  - Keeping it leaks the answer (undesired).
  - If later code assumes that print for debugging exists (e.g., tests), removing it could break those tests.

## Safe Enhancements (Won’t Break If Done Carefully)
- Convert user guesses to lowercase before checks.
- Validate that the user enters exactly one alphabetic character.
- Implement `'*'` to exit the game loop gracefully.
- Display the blanks as a joined string (e.g., `"a _ _ e"`) for readability.
- Hide the debug print of the chosen fruit.

## Discrepancies to Note
- The rules mention `'*'` to exit, but the game loop does not support it.
- The game currently prints the chosen fruit (likely a temporary debug aid).
