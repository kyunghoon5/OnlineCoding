# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def minmax(arr):
    # Use a breakpoint in the code line below to debug your script.
    sum = 0
    for i in arr:
        sum += i
    print(sum-max(arr), end ='')
    print('',sum-min(arr))

     # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    arr = list(map(int, input().rsplit()))
    minmax(arr)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
