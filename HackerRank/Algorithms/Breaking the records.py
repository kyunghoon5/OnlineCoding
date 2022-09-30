#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    h = scores[0]
    hcount = 0
    l = scores[0]
    lcount = 0
    for i in range(0, len(scores)):
        if h < scores[i]:
            h = scores[i]
            hcount += 1
    for i in range(0, len(scores)):
        if l > scores[i]:
            l = scores[i]
            lcount += 1
    return (hcount, lcount)
if __name__ == '__main__':
    fptr = sys.stdout

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
