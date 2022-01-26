"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730414608"

guess_word: str = input("Enter a 5-character word: ")
if len(guess_word) != 5: 
    print("Error: Word must contain 5 characters")
    exit()

letter: str = input("Enter a single character: ")

if len(letter) != 1:
    print("Error: Character must be a single character.")
    exit()
print("Searching for " + letter + " in " + guess_word)

instance: int = 0

if guess_word[0] == letter:
    print(letter + " found at index 0")
    instance = instance + 1
if guess_word[1] == letter:
    print(letter + " found at index 1")
    instance = instance + 1
if guess_word[2] == letter:
    print(letter + " found at index 2")
    instance = instance + 1
if guess_word[3] == letter:
    print(letter + " found at index 3")
    instance = instance + 1
if guess_word[4] == letter:
    print(letter + " found at index 4")
    instance = instance + 1

if instance == 1:
    print("1 instance of " + letter + " found in " + guess_word)
if instance == 2:
    print("2 instances of " + letter + " found in " + guess_word)
if instance == 0:
    print("No instances of " + letter + " found in " + guess_word)
if instance == 3:
    print("3 instances of " + letter + " found in " + guess_word)
if instance == 4:
    print("4 instances of " + letter + " found in " + guess_word)
if instance == 5:
    print("5 instances of " + letter + " found in " + guess_word)