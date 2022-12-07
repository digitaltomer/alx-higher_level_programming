#!/usr/bin/python3
def fizzbuzz():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("Fizzbuzz", end=" ")
        elif num % 3 == 0:
            print("Fizz", end=" ")
        elif num % 5 == 0:
            print("buzz", end=" ")
        else:
            print("{}".format(num), end=" ")
