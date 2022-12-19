#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    for k in my_list:
        if i < x:
            try:
                print(k, end="")
                i += 1
            except Exceptions:
                break

            print()
            return(i)
