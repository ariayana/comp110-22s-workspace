"""Dictionary related utility functions."""

__author__ = "730414608"


from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    
    file_handle = open(filename, "r", encoding="utf8")
    
    csv_reader = DictReader(file_handle)

    for row in csv_reader:
        result.append(row)
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]: 
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result


def head(c_table: dict[str, list[str]], row: int) -> dict[str, list[str]]:
    """The function will return a column-based table with only the number of rows of data for each column."""
    result: dict[str, list[str]] = {}
    for column in c_table:
        lista: list[str] = []
        i: int = 0
        while i < len(c_table[column]):
            if i < row:
                lista.append(c_table[column][i])
            i += 1
        result[column] = lista
        
    return result


def select(c_table: dict[str, list[str]], name: list[str]) -> dict[str, list[str]]:
    """This function will return a new column-based table with only a specific subset of the original columns."""
    result: dict[str, list[str]] = {}
    for header in name:
        result[header] = c_table[header]
        
    return result


def concat(c_table: dict[str, list[str]], d_table: dict[str, list[str]]) -> dict[str, list[str]]:
    """This function will return a new column-based table with two column-based tables combined."""
    result: dict[str, list[str]] = {}
    for column in c_table:
        result[column] = c_table[column]
    for column in d_table:
        if column in result:
            result[column] += d_table[column]
        else:
            result[column] = d_table[column]
    return result


def count(items: list[str]) -> dict[str, int]:
    """Given a list, this function will produce a dictionary where each key is a unqiue value in the given list and each value assicated is the count of the number of times that value appeared in the input list."""
    result: dict[str, int] = {}
    for name in items:
        if name in result:
            result[name] += 1
        else:
            result[name] = 1
    return result