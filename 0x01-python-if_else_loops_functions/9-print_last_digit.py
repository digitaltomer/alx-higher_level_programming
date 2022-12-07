#!/usr/bin/python3
def print_last_digit(number):
    if number <= 0 or number > 0:
        num_str = str(number)
        print(num_str[-1], end="")
        return num_str[-1]
