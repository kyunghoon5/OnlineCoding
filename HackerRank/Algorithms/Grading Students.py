#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    a = []
    for i in grades:
        if i > 38 and ((i%5) >= 3):
            i = (i+(5-(i%5)))
            a.append(i)
        elif i > 38 and ((i % 5) <= 2):
            a.append(i)
        elif i < 40 and ((40-i)>=3):
            a.append(i)
        elif i < 40 and ((40-i)<3):
            i= 40
            a.append(i)
    return a
if __name__ == '__main__':
    fptr = sys.stdout

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
