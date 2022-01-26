"""EX02 - One Shot Wordle."""

__author__ = "730414608"

secret: str = "python"

six_letter_guess: str = input("What is your 6-letter guess? ")

if len(six_letter_guess) != 6:
    print("That was not 6 letters! Try again: " + six_letter_guess)

WHITE_BOX: str = "\U00002B1C"
YELLOW_BOX: str = "\U0001F7E8"
GREEN_BOX: str = "\U0001F7E9"

index_of_guess: int = 0
emoji = ""
guess_character = False
alt_indices: int = 0

while index_of_guess < len(secret):
    if six_letter_guess[index_of_guess] == secret[index_of_guess]:
        emoji = emoji + GREEN_BOX
    else:
        guess_character = False
        alt_indices = 0
        while not guess_character and alt_indices < len(secret):
            if secret[alt_indices] == six_letter_guess[index_of_guess]:
                guess_character = True

            else:
                alt_indices = alt_indices + 1

        if guess_character:
            emoji = emoji + YELLOW_BOX
        else:
            emoji = emoji + WHITE_BOX
    index_of_guess = index_of_guess + 1
    
print(emoji)

if six_letter_guess != secret:
    print("Not quite. Play again soon!")
if six_letter_guess == secret:
    print("Woo! You got it!")