'''"Set an alarm 45 minutes early".

This method is simple. It is to change the time of the original set alarm to 45 minutes ahead. Because if you hear the alarm anyway, turn it off and you'll sleep a little better. This way, you will feel like you slept more every morning, and you won't be late for school.

If you use Changyeong's method when given the alarm time set by the current full-time employee, write a program to find out when to fix it.

input
Two integers H and M are given in the first line. (0 ≤ H ≤ 23, 0 ≤ M ≤ 59) And this means the alarm time H hours and M minutes set by the current full-time employee.

The input time uses a 24-hour expression. In 24-hour representation, a day starts at 0:0 (midnight) and ends at 23:59 (one minute before midnight the next day). When representing time, unnecessary zeros are not used.

output
In the first line, when Sang-geun uses Chang-young's method, the alarm time to be set is printed. (The output should be in the same format as the input.)'''

h, m = map(int, input().split())

if(m - 45 > 0):
    print(h, (m-45))
elif(m - 45 < 0):
    if(h-1 <0):
        print(24+(h-1), 60+(m-45))
    else:
        print(h-1, 60+(m-45))
elif(m - 45 ==0):
    print(h, (m-45))