"""Unit Testing Functions."""

__author__ = "730414608"

from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens_givenodd() -> None:
    """Edge Case: Given a list with only odd numbers, this function will return an empty list."""
    new_list: list[int] = [15, 17, 27, 29, 35, 67]
    assert only_evens(new_list) == []


def test_only_evens_oddeven() -> None:
    """Use Case: Given a list with even and odd numbers, this function will return a list with only evens."""
    new_list: list[int] = [1, 2, 3, 4, 5]
    assert only_evens(new_list) == [2, 4]


def test_only_evens_negativenum() -> None:
    """Use Case: Given a list with negative integers that are both even and odd, this function will return a list with only the negative evens."""
    new_list: list[int] = [-5, -18, -365, -1000]
    assert only_evens(new_list) == [-18, -1000]


def test_sub_empty() -> None:
    """Edge Case: Given a list with the length of 0 and the end index is <=0, this function will return a subset of the list that is empty."""
    new_list: list[int] = [5]
    assert sub(new_list, 0, 0) == []


def test_sub_middle() -> None:
    """Use Case: Given a list of integers, this function will return a subset of the given list that consists of the intergers in the middle of the list."""
    x_list: list[int] = [5, 10, 15, 20]
    assert sub(x_list, 1, 3) == [10, 15]


def test_sub_startneg() -> None:
    """Use Case: This function will return a subset of a given list of integers when the start index is negative."""
    n_list: list[int] = [-15, -150, -45, -200, -90, -890, -3, -9, -10, -560]
    assert sub(n_list, -5, 9) == [-15, -150, -45, -200, -90, -890, -3, -9, -10]


def test_concat_emptya() -> None:
    """Edge Case: Given two lists: the first list is empty, and the second list is not, this function will return a new list that will have the all elements of the second list."""
    a_list: list[int] = []
    b_list: list[int] = [5, 6]
    assert concat(a_list, b_list) == [5, 6]


def test_concat_ab() -> None:
    """Use Case: Given two lists of integers, this function will return a new list that will contain all elements of the first list followed by all of the elements of the second."""
    a_list: list[int] = [1, 2]
    b_list: list[int] = [5, 6]
    assert concat(a_list, b_list) == [1, 2, 5, 6]


def test_concat_xy() -> None:
    """Use Case: Given two lists of integers that have double and triple digits, this function will return a new list that will contain all elements of the first list followed by all of the elements of the second."""
    x_list: list[int] = [100, 2000]
    y_list: list[int] = [50, 60000]
    assert concat(x_list, y_list) == [100, 2000, 50, 60000]