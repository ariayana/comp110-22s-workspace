"""Unit Testing for EX06."""

__author__ = "730414608"

from dictionary import invert, favorite_color, count


def test_invert_emptydict() -> None:
    """Edge Case: Given an empty dictionary, the function will return an empty dictionary."""
    empty_dict: dict[str, str] = {}
    assert invert(empty_dict) == {}


def test_invert_chardict() -> None:
    """Use Case: Given a dictionary with one character as the key and value, the function will invert the key and its value."""
    small_dict: dict[str, str] = {'a': 'z', 'b': 'y', 'c': 'x'}
    assert invert(small_dict) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_invert_worddict() -> None:
    """Use Case: Given a dictionary with words as the key and value, the function will invert the key and its value."""
    word_dict: dict[str, str] = {'apple': 'cat', 'zoey': 'mark', 'heel': 'tar'}
    assert invert(word_dict) == {'cat': 'apple', 'mark': 'zoey', 'tar': 'heel'}


def test_favorite_color_tie() -> None:
    """Edge Case: Given a dictionary where two values are appear the same number of times, this function will return the color that appeared in the dictionary first."""
    favored: dict[str, str] = {"Marc": "yellow", "Ari": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(favored) == "yellow"


def test_favorite_color_winner() -> None:
    """Use Case: Given a dictionary of friends as keys and their favorite colors as values, this function will return the most popular color."""
    favored: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(favored) == "blue"


def test_favorite_color_moreoptions() -> None:
    """Use Case: Given a dictionary where a key has more values (color name) than another key, this function will return the value of the key with the most values."""
    favored: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue", "Ari": "brown", "Savannah": "green", "Nyjeria": "yellow", "Grandma": "purple", "Lexi": "brown", "Rue": "brown"}
    assert favorite_color(favored) == "brown"


def test_count_emptylist() -> None:
    """Edge Case: Given an empty list, this function would return an empty dictionary."""
    empty_list: list[str] = []
    assert count(empty_list) == {}


def test_count_objects() -> None:
    """Use Case: Given a list of objects, this function will return a dictionary with the items and the number of times it appears in the list."""
    objects: list[str] = ["ball", "ball", "shoe", "toy", "doll"]
    assert count(objects) == {"ball": 2, "shoe": 1, "toy": 1, "doll": 1}

 
def test_count_names() -> None:
    """Use Case: Given a list of names, this function will return a dictionary with the names and the number of times it appears in the list."""
    names: list[str] = ["Ari", "Jess", "Kris"]
    assert count(names) == {"Ari": 1, "Jess": 1, "Kris": 1}