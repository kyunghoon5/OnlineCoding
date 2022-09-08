'''Write a program that, given a year, prints 1 if it is a leap year, or 0 otherwise.

A leap year is when the year is a multiple of 4 but not a multiple of 100 or a multiple of 400.

For example, 2012 is a leap year because it is a multiple of 4 and not a multiple of 100. The year 1900 is not a leap year because it is a multiple of 100 and not a multiple of 400. However, the year 2000 is a leap year because it is a multiple of 400.

input
The year is given in the first line. year is a natural number greater than or equal to 1 and less than or equal to 4000.

output
The first line prints 1 if it is a leap year, and 0 otherwise.'''

leap = int(input())

if (leap % 4 == 0 and leap % 100 != 0) or (leap % 400 == 0):
    print("1")
else:
    print("0")
