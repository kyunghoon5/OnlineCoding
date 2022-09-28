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
    data0 = []
    data1 = []
    cm =[]
    for i in range(1, b[0] + 1):
        data0.append(i*a[0])
    print(data0)
    for i in range(1, b[0] + 1):
        data1.append(i*a[1])
    print(data1)

    for i in data0:
        if i in data1:
            cm.append(i)
    print(cm)

    q=[]
    for i in b:
        for k in range(a[-1],b[0]+1):
            if i%k == 0:
                q.append(k)
    print(q)


    data11 =[]
    for i in q:
        if i in cm:
            data11.append(i)
    print(data11)
    return len(data11)

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
