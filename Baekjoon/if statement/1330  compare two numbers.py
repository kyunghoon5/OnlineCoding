'''
Problem
Given two integers A and B, write a program that compares A and B.

input
A and B are given in the first line. A and B are separated by a space.

Print
The first line prints one of three things:

If A is greater than B, '>' is output.
If A is less than B, '<' is output.
If A and B are the same, '==' is output.
'''


A, B = map(int, input().split())

if A < B:
    print("<")
elif A > B:
    print(">")
else:
    print("==")
