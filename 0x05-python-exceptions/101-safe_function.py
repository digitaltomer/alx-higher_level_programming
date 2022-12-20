#!/usr/bin/python3
import sys

try:
    result = fct(*args)
    return (result)
except:
    print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
    return(None)
