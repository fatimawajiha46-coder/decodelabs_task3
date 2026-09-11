"""
Project 3: Random Password Generator
--------------------------------------
Why it matters: Teaches how to use Python's built-in libraries to solve
real-world security problems, instead of writing everything from scratch.

Key Skill: Importing Modules (import random) & String manipulation.
"""

import random
import string


def generate_password(length):
    """Build a random password of the given length using letters, digits, and symbols."""
    # string manipulation: combine character sets into one pool to pick from
    letters = string.ascii_letters      # a-z, A-Z
    digits = string.digits              # 0-9
    symbols = "!@#$%^&*()-_=+"

    all_characters = letters + digits + symbols

    password_characters = []

    # Guarantee at least one of each type, so the password is genuinely complex
    password_characters.append(random.choice(letters))
    password_characters.append(random.choice(digits))
    password_characters.append(random.choice(symbols))

    # Fill the rest of the length with random characters from the full pool
    remaining_length = length - len(password_characters)
    for _ in range(remaining_length):
        password_characters.append(random.choice(all_characters))

    # Shuffle so the guaranteed characters aren't always in the same spot
    random.shuffle(password_characters)

    # join(): turn the list of characters back into one string
    password = "".join(password_characters)
    return password


def get_length_from_user():
    while True:
        entry = input("How many characters should the password be? (minimum 4): ").strip()
        try:
            length = int(entry)
            if length < 4:
                print("Please choose a length of at least 4.")
                continue
            return length
        except ValueError:
            print("Please enter a whole number (e.g., 8).")


def main():
    print("--- RANDOM PASSWORD GENERATOR ---")
    length = get_length_from_user()

    password = generate_password(length)

    print(f"\nYour generated password ({length} characters):")
    print(password)


if __name__ == "__main__":
    main()
