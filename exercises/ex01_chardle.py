"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730414608"
guess_word: str = input("Enter a 5-character word: ")
if len(guess_word) != 5: 
    print("Error: Word must contain 5 characters")
    exit()
letter: str = input("Enter a single character: ")
print("Searching for " + letter "in " + guess_word)
if len(letter) != 1:
    print("Error: Character must be a single character.")
    exit()
if guess_word[0] == letter:
    print(letter + " found at index 0")
if guess_word[1] == letter:
    print(letter + " found at index 1")
if guess_word[2] == letter:
    print(letter + " found at index 2")
if guess_word[3] == letter:
    print(letter + " found at index 3")
if guess_word[4] == letter:
    print(letter + " found at index 4")
instance: int = int(letter == letter) 
print((instance) + " of" letter "is found in" + guess_word)