#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    h = s[:2]
    m = s[3:5]
    k = s[6:8]
    t = s[-2:]

    if t == "PM":
        if h =="12":
            return f'{h}:{m}:{k}'
        else:
            r_h =int(h) + 12
            r_h = str(r_h)
            return f'{r_h}:{m}:{k}'

    if t == "AM":
        if h =="12":
            h= "00"
        return f'{h}:{m}:{k}'



if __name__ == '__main__':
    fptr = sys.stdout

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
