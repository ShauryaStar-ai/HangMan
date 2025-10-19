import random
import sys

"""
Dinosaur Name Guessing Game

- Inspired by `HangMan.py` fruit guessing game structure
- Adds difficulty selection (Easy, Medium, Hard) that controls:
  - The pool of dinosaur names by length/obscurity
  - The number of lives
  - Hint availability
- Clean control flow with `controller()` entrypoint

How to run (Windows PowerShell):
  python dinoGame.py

"""

EASY_DINOS = ["trex", "raptor", "dino", "spino", "stego", "ankyl"]

MEDIUM_DINOS = [
    "triceratops",
    "velociraptor",
    "brachiosaurus",
    "stegosaurus",
    "allosaurus",
]

HARD_DINOS = [
    "parasaurolophus",
    "pachycephalosaurus",
    "therizinosaurus",
    "micropachycephalosaurus",
]

DIFFICULTY_CONFIG = {
    "easy": {"lives": 7, "pool": EASY_DINOS, "hint": True},
    "medium": {"lives": 5, "pool": MEDIUM_DINOS, "hint": True},
    "hard": {"lives": 4, "pool": HARD_DINOS, "hint": False},
}


def get_consent() -> str:
    consent = input("Do you want to play the dinosaur name guessing game? (y/n): ")
    consent = consent.strip().lower()
    while consent not in ("y", "n"):
        print("Invalid input, try again.")
        consent = input("Play the dinosaur name guessing game? (y/n): ")
        consent = consent.strip().lower()
    return consent


def choose_difficulty() -> str:
    print("Choose difficulty: easy | medium | hard")
    difficulty = input("Enter difficulty: ")
    difficulty = difficulty.strip().lower()
    while difficulty not in DIFFICULTY_CONFIG:
        print("Invalid difficulty. Choose from: easy, medium, hard")
        difficulty = input("Enter difficulty: ")
        difficulty = difficulty.strip().lower()
    return difficulty


def pick_secret_word(words: list[str]) -> str:
    index = random.randint(0, len(words) - 1)
    return words[index]


def format_progress(progress_chars: list[str]) -> str:
    return " ".join(progress_chars)


def show_rules(pool: list[str], lives: int) -> None:
    print("-" * 150)
    print("Welcome to the Dinosaur Name Guessing Game")
    print(
        f"You will guess letters of a randomly selected dinosaur name from a pool of {len(pool)} names."
    )
    print("Enter one letter at a time.")
    print("You can exit at any time by entering '*'.")
    print(f"You have {lives} lives. A wrong letter costs one life.")
    print("-" * 150)


def get_hint(secret_word: str, current_progress: list[str], guessed: set[str]) -> str:
    for ch in secret_word:
        if ch not in guessed:
            return ch
    return ""


def game(pool: list[str], lives: int, allow_hint: bool) -> None:
    secret_word = pick_secret_word(pool)
    # print(secret_word)  # Uncomment for debugging
    progress_chars = ["_" for _ in secret_word]
    guessed_letters: set[str] = set()

    print(format_progress(progress_chars))

    while lives > 0 and "_" in progress_chars:
        user_input = input("Enter a letter (or '*' to quit, '?' for hint): ")
        user_input = user_input.strip().lower()

        if user_input == "*":
            print("Game exited. See you next time!")
            return

        if user_input == "?":
            if allow_hint:
                hint_letter = get_hint(secret_word, progress_chars, guessed_letters)
                if hint_letter:
                    print(f"Hint: Try the letter '{hint_letter}'.")
                else:
                    print("No hints available; you've uncovered or tried all letters.")
            else:
                print("Hints are disabled for this difficulty.")
            continue

        if not user_input.isalpha() or len(user_input) != 1:
            print("Please enter a single alphabetic character.")
            continue

        if user_input in guessed_letters:
            print("You've already tried that letter. Current:")
            print(format_progress(progress_chars))
            continue

        guessed_letters.add(user_input)

        if user_input in secret_word:
            for index, letter in enumerate(secret_word):
                if letter == user_input:
                    progress_chars[index] = user_input
            print("Nice! You revealed letter(s):")
            print(format_progress(progress_chars))
        else:
            lives -= 1
            print("Wrong guess. You lost a life.")
            print(f"Lives left: {lives}")
            print(format_progress(progress_chars))

        if "_" not in progress_chars:
            print(f"Success! You guessed the dinosaur: {secret_word}")
            return

    if lives == 0 and "_" in progress_chars:
        print(f"Out of lives. The dinosaur was: {secret_word}")


def controller() -> None:
    if get_consent() != "y":
        print("Have a good day. Let's play next time.")
        return

    difficulty = choose_difficulty()
    config = DIFFICULTY_CONFIG[difficulty]
    pool = config["pool"]
    lives = config["lives"]
    allow_hint = config["hint"]

    show_rules(pool, lives)
    game(pool, lives, allow_hint)


if __name__ == "__main__":
    try:
        controller()
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit(0)
