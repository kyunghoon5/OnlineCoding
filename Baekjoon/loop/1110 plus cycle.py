'''When an integer greater than or equal to 0 and less than or equal to 99 is given, the following operation can be performed. First, if the given number is less than 10, add a leading zero to make it a two-digit number, and add each digit. Then, a new number can be formed by concatenating the rightmost digit of the given number and the rightmost digit of the sum obtained earlier. Let's look at the following example.

It starts at 26. 2+6 = 8. The new number is 68. 6+8 = 14. The new number is 84. 8+4 = 12. The new number is 42. 4+2 = 6 The new number is 26.

The above example can return to the original number after 4 times. Thus, the length of the cycle of 26 is 4.

Given N, write a program to find the length of N cycles.
'''
a = int(input()) # 26
match = a
count = 0

while True:
    num = match // 10  # 2 6 8 4
    num2 = match % 10  # 6 8 4 2
    total = (num + num2) % 10 #total 8  4 2 6
    match = (num2 * 10) + total #match 68 84 42 26

    count = count + 1
    if(match == a):
        break
print(count)


