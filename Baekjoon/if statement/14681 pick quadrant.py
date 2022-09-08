'''One common math problem is to figure out which quadrant a given point belongs to. Quadrants are numbered from 1 to 4 as shown in the figure below. "Quadrant n" means "the nth quadrant".



For example, a point A having a coordinate of (12, 5) belongs to the first quadrant because both the x-coordinate and the y-coordinate are positive numbers. Point B belongs to the second quadrant because the x-coordinate is negative and the y-coordinate is positive.

Write a program that takes the coordinates of a point as input and finds out which quadrant the point belongs to. However, it is assumed that both the x-coordinate and the y-coordinate are positive or negative.

input
The first line is given an integer x. (−1000 ≤ x ≤ 1000; x ≠ 0) The next line is given an integer y. (−1000 ≤ y ≤ 1000; y ≠ 0)

output
Print the quadrant number (one of 1, 2, 3, or 4) of the point (x, y).'''

x = int(input())
y = int(input())

if (x > 0 and y > 0):
    print("1")
elif (x < 0 and y >0):
    print("2")
elif (x < 0 and y <0):
    print("3")
else:
    print("4")