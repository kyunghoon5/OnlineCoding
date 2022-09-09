'''There is a game where three dice with eyes 1 to 6 are rolled and the prize money is awarded according to the following rules.

If there are 3 identical eyes, you will receive a prize of 10,000 won + (same eye) x 1,000 won.
If there are only two identical eyes, you will receive a prize of 1,000 won + (same eye) x 100 won.
If all eyes are different, (the largest one among them) will receive a prize of 100 won.
For example, given 3 eyes 3, 3, and 6, the prize money is calculated as 1,000+3×100 and you get 1,300 won. Also, if 3 eyes are given as 2, 2, 2, it is calculated as 10,000+2×1,000 and you will receive 12,000 won. If 3 eyes are given as 6, 2, and 5, the largest value among them is 6, so it is calculated as 6×100 and you will receive 600 won as a prize money.

Write a program that calculates the prize money when three dice are rolled.

input
In the first row, three eyes are each given with a space between them.

output
The first line prints the prize money of the game.'''

a, b, c = map(int, input().split())

if a == b == c:
    print(10000 + a * 1000)
elif (a == b != c):
    print(1000 + a * 100)
elif (a == c != b):
    print(1000 + a * 100)
elif (b == c != a):
    print(1000 + b * 100)
elif (a != b != c):
    print(max(a,b,c) *100)