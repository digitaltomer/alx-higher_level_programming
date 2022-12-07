#!/usr/bin/python3
for i in range(100):
    if i < 10:
        i = str(i).zfill(2)
    if i == 99:
        print(i)
        break
    print("{}".format(i), end=", ")
