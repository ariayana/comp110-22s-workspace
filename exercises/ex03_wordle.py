"""EX 03 - One-Player Worlde."""

__author__ = "730414608"


def contains_char(searching: str, expected_char: str) -> bool:
    """The function's purpose is to search for a single character (a) in a str of any length (b), so that if a is found in b, it will return True and if not, False."""
    assert len(expected_char) == 1
    index_of_guess: int = 0

    while index_of_guess < len(searching):
        if searching[index_of_guess] == expected_char:
            return True
        else:
            index_of_guess = index_of_guess + 1
    return False    


def emojified(guess: str, secret: str) -> str:
    """This function would tell us the emoji that would correspond to the correct character at the correct position, correct character at a different position, or if the character is not found at all in the secret word."""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    YELLOW_BOX: str = "\U0001F7E8"
    GREEN_BOX: str = "\U0001F7E9"
    i: int = 0
    emoji = ""
    
    while i < len(guess):
        if guess[i] == secret[i]:
            emoji = emoji + GREEN_BOX
        else:
            if contains_char(secret, guess[i]):
                emoji = emoji + YELLOW_BOX
            else:
                emoji = emoji + WHITE_BOX
        i = i + 1
    return emoji


def input_guess(expected_length: int) -> str:
    """The purpose of this function on to prompt the user for an input that has an integer of an expected legnth and continue to prompt them until the expected length is given."""
    guess: str = input(f"Enter a {expected_length} character word: ")
    while expected_length != len(guess):
        guess = input(f"That wasn't a {expected_length} char! Try again: ")
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret: str = "codes"
    current_turn: int = 1
    playing: bool = True
    while current_turn < 7 and playing:
        print(f"=== Turn {current_turn}/6 ===")
        user_input: str = input_guess(len(secret)) 
        print(emojified(user_input, secret))
        if user_input == secret:
            print(f"You won in {current_turn}/6 turns!")
            playing = False
        else:
            current_turn = current_turn + 1
            
    if current_turn == 7:
        print("X/6 - Sorry, try again tomorrow!")
 
    
if __name__ == "__main__":
    main()