a = int(input())
n = []
for i in range(a):
    m = list(map(int,input().split()))
    n += m
n.sort()
print(*n, sep='\n')