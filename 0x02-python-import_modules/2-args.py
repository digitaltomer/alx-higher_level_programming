#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    num_of_args = len(sys.argv) - 1

    if num_of_args == 0:
        print("{} arguments.".format(num_of_args))
    elif num_of_args == 1:
        print("{} argument:".format(num_of_args))
        print("{}: {}".format(num_of_args, sys.argv[1]))
    else:
        print("{} arguments:".format(num_of_args))
        # loop through the list and print
        for i in range(num_of_args + 1):
            if i != 0:
                print("{}: {}".format(i, sys.argv[i]))
