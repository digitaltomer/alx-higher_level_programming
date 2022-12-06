#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for list_ in matrix:
        for element in list_:
            if element != list_[-1]:
                print("{:d}".format(element), end=" ")
            else:
                print("{:d}".format(element), end="")
        print()
