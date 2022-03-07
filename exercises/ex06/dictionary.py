"""Implementing function skeletons and implementations for EX06."""

__author__ = "730414608"


def invert(a: dict[str, str]) -> dict[str, str]:
    """Given a dictionary with strings as the keys and values, this function will return a dictionary that inverts the keys and values such that the keys of the input list becomes the values of the output list."""
    result: dict[str, str] = {}
    for key in a:
        if a[key] in result:
            raise KeyError('Your dictionary cannot have repeated key names.')
        else:
            result[a[key]] = key
    return result


def favorite_color(names_color: dict[str, str]) -> str:
    """This function will return the name of the color that appears the most frequent in a given dictionary."""
    result: str = ""
    popular_color: dict[str, int] = {}
    for key in names_color:
        color = names_color[key]
        if color in popular_color:
            popular_color[color] += 1
        else:
            popular_color[color] = 1
    value: int = 0
    for key in popular_color:
        if popular_color[key] > value:
            result = key
            value = popular_color[key]
    return result


def count(freq: list[str]) -> dict[str, int]:
    """Given a list of strings, this function will produce a dictionary of keys as strings with value types of integers where each key is a unique value in the given list and each value is associated is the count of the number of times that value appeared in the input list."""
    result: dict[str, int] = {}
    for items in freq:
        if items in result:
            result[items] += 1
        else:
            result[items] = 1
    return result
