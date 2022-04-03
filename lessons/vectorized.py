from __future__ import annotations

from typing import Union


class StrArray:
    items: list[str]

    def __init__(self, a):
        self.items = a
    
    def __repr__(self) -> str:
        return f"StrArray({self.items})"

    def __add__(self, rhs: Union[str, StrArray]) -> StrArray:
        """Add is a vectorized operation that applies to all items.
        When rhs is a str, it is concatenated to every item in a new StrArray.
        """
        # Establish a result list of strings that is empty
        result: list[str] = []
        if isinstance(rhs, str):
            # Loop through every item in self.items
            for item in self.items:
                # Append the concatentation of item with rhs to your result list
                result.append(item + rhs)
        else:
            for i in range(0, len(self.items)):
                result.append(self.items[i] + rhs.items[i])
        # After loop, return a new StrArray object constructed with result list
        return StrArray(result)


first: StrArray = StrArray(["Armando", "Brady", "Caleb"])
last: StrArray = StrArray(["Bacot", "Manek", "Love"])
print(first + "!")
print(first + last)
print(last + ", " + first)
print(last + "//" + first)