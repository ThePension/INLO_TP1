"""
Module that gathers methods to manipulate strings
"""


def upper_case(input_string: str) -> str:
    """
    Returns the upper case version of an input string
    """
    if not isinstance(input_string, str):
        raise TypeError("Please provide a string argument")
    return input_string.upper()


def lower_case(input_string: str) -> str:
    """
    Returns the lower case version of an input string
    """
    if not isinstance(input_string, str):
        raise TypeError("Please provide a string argument")
    return input_string.lower()


def invert(input_string: str) -> str:
    """
    Inverts a string
    """
    if not isinstance(input_string, str):
        raise TypeError("Please provide a string argument")
    return input_string[::-1]
