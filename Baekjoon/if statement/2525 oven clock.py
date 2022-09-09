'''Write a program that calculates the time at which the roasting ends when the start time of roasting smoked duck and the time required for roasting in the oven are given in minutes.

input
The first line shows the current time. The current time is given in the order of hour A (0 ≤ A ≤ 23) and minute B (0 ≤ B ≤ 59) as integers with a space between them. In the second line, the time required to cook C (0 ≤ C ≤ 1,000) is given in minutes.

output
In the first line, the hour and minute of the end time are printed with a space between them. (However, the hour is an integer from 0 to 23, and the minute is an integer from 0 to 59. In a digital clock, 0:0 after 23:59 to 1 minute.)
'''
h, m = map(int, input().split())
timer = int(input())

h += timer // 60
m += timer % 60

if m >= 60:
    h += 1
    m -= 60
if h >= 24:
    h -= 24
print(h, m)








