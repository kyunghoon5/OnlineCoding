'''input
The first line gives the total amount of $X$ on the receipt.

The second line gives the number $N$ of the type of item purchased on the receipt.

After that, in the $N$ lines, the price $a$ and the number $b$ of each item are given with a space between them.

output
If the total amount calculated by the price and number of items purchased matches the total amount written on the receipt, Yes is output. If they do not match, output No.
'''
n = int(input())
y = int(input())


total = 0

for i in range(1, y+1):
    a, c = map(int, input().split())
    sum = a*c
    total += sum
if total == n:
    print("Yes")
else:
    print("No")
