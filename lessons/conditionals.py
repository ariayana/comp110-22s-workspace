"""An exmaple of conditonal (if-else) statments."""

SECRET: int = 3

print("I am thinking of a value between 1-5, what is it?")
guess: int = int(input("What is your guess? "))

if guess == SECRET:
    print("You guessed correctly!!!")
    print("Have a wonderful day!!!")
else:
    print("Sorry, you guessed incorrectly :(")
    if guess > SECRET:
        print("You guessed to high!")
    else:
        print("You guessed too low!")
print("Game over.")