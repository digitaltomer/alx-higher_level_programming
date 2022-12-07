#!/usr/bin/python3
def uppercase(str):
    str2 = ""
    for i in str:
        if 96 < ord(i) < 123:
            i = chr(ord(i) - 32)
            str2 += i
        else:
            str2 += i
    print("{}".format(str2))
