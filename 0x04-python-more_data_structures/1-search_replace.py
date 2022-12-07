#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq = [*set(my_list)]
    u_sum = 0

    for i in uniq:
        u_sum += i
    return (u_sum)
# plist = [1, 2, 3, 4, 2, 1, 5, 3]
# print(uniq_add(plist))
