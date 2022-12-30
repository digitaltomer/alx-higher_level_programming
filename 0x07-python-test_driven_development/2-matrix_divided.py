#!/usr/bin/python3
"""
This module has a function that divides all element of a matrix
"""


def matrix_divided(matrix, div):
   """Return a new matrix after all elements have been divided by 2, rounded to 2 decimal places
   Arg:
      matrix: matrix must be a list of lists of integers or floats
      div: Number to be used for the division (can be a float or an integer)
   Raises:
       TypeError: If the matrix contains integers/floats
       TypeError: If the matrix contains rows of different sizes
       TypeError: If div is not a number
       ZeroDivisionError: If div is 0
   Returns:
       A new matrix after all elements have been divided by 2
   """
   if (not isinstance(matrix, list) or matrix == [] or
           not all(isinstance(row, list) for row in matrix) or
           not all((isinstance(element, int) or isinstance(element, float))
               for element in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of"
                        "integers/floats")

   if not all(len(row) == len(matrix[0]) for row in matrix):
       raise TypeError("Each row of the matrix must have the same size")

   if not isinstance(div, int) and not isinstance(div, float):
       raise TypeError("div must be a number")

   if div == 0:
       raise ZeroDivisionError("division by zero")

   return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
