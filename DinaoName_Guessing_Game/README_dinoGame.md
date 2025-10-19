# Dinosaur Name Guessing Game - Documentation

## Overview
This project implements a command-line dinosaur name guessing game inspired by `HangMan.py`. The player guesses letters of a secret dinosaur name selected at random. The game provides lives, input validation, and optional hints depending on difficulty.

## How to Run
From the `DinaoName_Guessing_Game` directory, run:

```bash
python dinoGame.py
```

## Gameplay
- The game asks for consent to start.
- The player selects a difficulty: `easy`, `medium`, or `hard`.
- A dinosaur name is chosen from a difficulty-specific pool.
- The player guesses one letter per turn:
  - Correct guesses reveal all matching positions.
  - Incorrect guesses cost one life.
  - Enter `*` to exit immediately.
  - Enter `?` for a hint (if enabled by difficulty).
- The game ends when the word is fully revealed or lives reach zero.

## Difficulty Settings
- easy: 7 lives, short/common names, hints enabled
- medium: 5 lives, longer names, hints enabled
- hard: 4 lives, long/obscure names, hints disabled

## Files
- `dinoGame.py`: Main game logic with `controller()` entrypoint.
- `README_dinoGame.md`: This documentation.
- `task.md`: Original task requirements.

## Performance Notes
- The game uses O(n) operations per guess over the secret name length to reveal letters.
- Memory usage is small: a list of progress characters and a set of guessed letters.
- Random selection is uniform over the chosen pool.

## Extensibility
- Add or adjust dinosaur lists in `EASY_DINOS`, `MEDIUM_DINOS`, `HARD_DINOS`.
- Change lives/hint rules via `DIFFICULTY_CONFIG`.
- To localize messages, extract strings into a map and reference them in I/O functions.

## Potential Breaking Changes
If you modify the following areas, you may break the game flow or cause errors:
- Renaming `controller()` or removing the `if __name__ == "__main__":` block will break direct execution.
- Changing `DIFFICULTY_CONFIG` keys without updating `choose_difficulty()` validation will reject valid inputs or accept invalid ones.
- Setting lives to non-positive values will make the game unwinnable or instantly end.
- Providing an empty pool in any difficulty will cause `random.randint` to fail.
- Removing input validation (single alphabetic character) may allow unexpected states.

## Testing Tips
- Temporarily print the secret word (uncomment the debug print in `game`) to quickly verify reveal logic.
- Try repeated guesses to ensure duplicate handling works.
- Check `?` hint behavior on each difficulty.
- Verify `*` exits cleanly without tracebacks.
