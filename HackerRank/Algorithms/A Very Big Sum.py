#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'aVeryBigSum' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER_ARRAY ar as parameter.
#

def aVeryBigSum(ar):
    # Write your code here
    long = 0
    for i in range(ar_count):
        long += ar[i]
    return long


if __name__ == '__main__':
    fptr = sys.stdout

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
