#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    count = 0
    count1 = 0
    count2 = 0
    for i in arr:
        if i > 0:
            count += 1
        if i == 0:
            count1 += 1
        if i < 0:
            count2 += 1
    print("{:.6f}".format(count/n))
    print("{:.6f}".format(count2 / n))
    print("{:.6f}".format(count1 / n))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
