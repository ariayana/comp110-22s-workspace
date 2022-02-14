"""Some examples of tender, loving function definitions."""


def love(name: str) -> str:
    """Given a name as a parameter, returns a loving string."""
    return f"I love you {name}!"

# from lessons.love_functions import love to import to REPL and can practice with it in the terminal
# function call love("Holly") for example result: str = love("Holly") and returns I love you Holly
# quit() and start over in REPL, so you can update changes you made in functions that will save in the REPL.


def spread_love(to: str, n: int) -> str:
    """Generates a string that repeats a loving message n times."""
    love_note: str = ""
    counting: int = 0
    while counting < n:
        love_note += love(to) + "\n"
        # += means add on to. and since we want to add on to this str, that is why we use +=
        # love(to)- we do not need to say love(to: str) since to is already said to a string, python will know that to mataches to the "to" in the defintion of spread_love. They match, they should match.
        # print in order to get rid the \n
        counting = counting + 1
        # can also say counting += 1
    return love_note
    # make sure to place return outside of the while loop, so line it up with the indentation of while