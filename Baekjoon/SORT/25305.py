a, b = map(int, input().split())
c = list(map(int, input().split()))
d = sorted(c, reverse=True)
print(d[b-1])