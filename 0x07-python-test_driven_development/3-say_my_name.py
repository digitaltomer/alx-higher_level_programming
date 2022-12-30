#!/usr/bin/python3
"""
This function prints a first name and last name
"""


def say_my_name(first_name, last_name=""):
    """Return a first name and last name as a string
    Arg:
        first_name: is the first name as a string
        last_name: is the last name as a string
    Raises:
          TypeError: first or last name must be a string
    Prints:
          My name is <first name> <last name>
    """
    if not isinstance(first_name, str) or not isinstance(last_name, str):
        raise TypeError("first_name must be a string"
                         "or last_name must be a string")
    print (f"My name is {first_name} {last_name}")
