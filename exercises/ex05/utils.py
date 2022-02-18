"""Implementing function skeletons."""

__author__ = "730414608"


def only_evens(record: list[int]) -> list[int]:
    """Only return the even numbers in a given list."""
    i: int = 0
    new_list: list[int] = []
    while i < len(record):
        if record[i] % 2 == 0:
            new_list.append(record[i])
        i += 1
    return new_list


def sub(name: list[int], start: int, end: int) -> list[int]:
    """Return a subset list from a given list."""

    subset_list: list[int] = []
    if len(name) == 0 or start > len(name) or end <= 0:
        return []
    if start < 0:
        start = 0
    if end > len(name):
        end = len(name)

    while start < end:
        subset_list.append(name[start])
        start += 1
    return subset_list


def concat(listx: list[int], listy: list[int]) -> list[int]:
    """Return a list that contains items from the first list follwed by the second list."""
    new_list: list[int] = []
    new_list = listx
    i: int = 0
    while i < len(listy):
        new_list.append(listy[i])
        i += 1
    return new_list