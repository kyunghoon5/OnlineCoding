'''
Write a program that receives test scores and outputs A for 90 to 100, B for 80 to 89, C for 70 to 79, D for 60 to 69, and F for the rest of the scores.

input
The test scores are given in the first line. The test score is an integer greater than or equal to 0 and less than or equal to 100.

output
Print the test results.
'''

score = int(input())

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")