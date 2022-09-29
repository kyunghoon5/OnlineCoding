#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#


def getTotalX(a, b):
    # Write your code here
    dataa = []
    datab = []
    len_ = len(a+b)
    cm =[]

    for i in range(1, 101):
        for number_a in a:
            if i % number_a == 0:
                dataa.append(i)
        for number_b in b:
            if number_b % i ==0:
                datab.append(i)
                total = dataa + datab

    for i in total:
        if total.count(i) == len_:
          cm.append(i)

    return len(set(cm))




if __name__ == '__main__':
    fptr = sys.stdout

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
