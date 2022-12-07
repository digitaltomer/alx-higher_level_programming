#!/usr/bin/python3
def uppercase(str):
    for c in str:
        str1 = ""
        if 96 < ord(c) < 123:
            i = chr(ord(c) - 32)
            str1 += c
        else:
            str1 += c
    print("{}".format(str1))
