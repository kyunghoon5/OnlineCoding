n = int(input())


for i in range(n):
    arr = input()
    total = 0
    reset = 0
    for j in range(len(arr)):
        if arr[j] == 'O':
            total += 1
            reset += total
        elif arr[j] == 'X':
            total = 0
    print(reset)
