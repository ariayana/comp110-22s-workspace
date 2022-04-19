"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730414608"


class Simpy:
    """Creates a new object of typee Simpy."""
    values: list[float]

    def __init__(self, a: list[float]):
        """Initializes the values attribute of the newly constructed Simpy object to the argument passed in."""
        self.values = a

    def __str__(self) -> str:
        """Method will be called automagically when a Simpy object is conveerted to a str representation."""
        result: str = ""
        for i in range(0, (len(self.values))):
            if i == (len(self.values) - 1):
                result = result + str(self.values[i])
            else:
                result = result + str(self.values[i]) + ", "
        
        return f"Simpy([{result}])"

    def fill(self, value: float, num: int) -> None:
        """After calling this method, the length of the Simpy object's values should be equal to the second argument given to this method."""
        self.values: list[float] = []
        for v in range(0, num):
            self.values.append(value)
    
    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Purpose: Is to fill in the values attribute with range values, but in terms of floats. Basically putting floats in order from leeast to greatest."""
        assert step != 0.0
        self.values: list[float] = []

        if step > 0:
            while start < stop:
                self.values.append(start)
                start += step
        if step < 0: 
            while start > stop:
                self.values.append(start)
                start += step

    def sum(self) -> float:
        """Computes and returns the sum of all items in the values attribute."""
        result: float = 0.0 
        
        result = sum(self.values)
        return result

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Returns a new Simpy object and should not mutate the object the method it is called on."""
        i: int = 0
        result: Simpy = Simpy([])
        
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            while i < len(self.values):
                result.values.append(self.values[i] + rhs.values[i])
                i += 1
        else:
            while i < len(self.values):
                result.values.append(self.values[i] + rhs)
                i += 1
        
        return result

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Gives us the ability to use the power operator in conjunction with Simpy objects and floats."""
        i: int = 0
        result: Simpy = Simpy([])
        
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            while i < len(self.values):
                result.values.append(self.values[i] ** rhs.values[i])
                i += 1
        else:
            while i < len(self.values):
                result.values.append(self.values[i] ** rhs)
                i += 1
        
        return result

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Gives us the ability to produce a mask based on the equality of each item in the values attribute with some other Simpy object or a float value."""
        i: int = 0
        result: list[bool] = []
        
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            while i < len(self.values):
                if self.values[i] == rhs.values[i]:
                    result.append(True)
                    i += 1
                else:
                    result.append(False)
                    i += 1
        else:
            while i < len(self.values):
                if self.values[i] == rhs:
                    result.append(True)
                    i += 1
                else: 
                    result.append(False)
                    i += 1
        return result

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """This operator will give us the ability to compare each item in the values attribute and see which one is the greater value."""
        i: int = 0
        result: list[bool] = []
        
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            while i < len(self.values):
                if self.values[i] > rhs.values[i]:
                    result.append(True)
                    i += 1
                else:
                    result.append(False)
                    i += 1
        else:
            while i < len(self.values):
                if self.values[i] > rhs:
                    result.append(True)
                    i += 1
                else: 
                    result.append(False)
                    i += 1
        return result

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Gives us the ability to read specific items from the Simpy array."""
        if isinstance(rhs, list):
            result: Simpy = Simpy([])
            assert len(self.values) == len(rhs)
            for i in range(0, len(self.values)):
                if rhs[i]:
                    result.values.append(self.values[i])
            return result

        else:
            r: float = 0.0
            r += self.values[rhs]
            return r