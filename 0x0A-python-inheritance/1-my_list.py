#!/usr/bin/python3
"""This module prints a list but sorted"""


class Mylist(list):
    """A class that inherits from list"""
    def print_sorted(self):
        """prints a sorted list"""
        print(sorted(self))
