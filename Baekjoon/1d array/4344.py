n = int(input())

for i in range(n):
    m = list(map(int,input().split()))
    count = 0
    for j in m[1:]:
        ave = sum(m[1:]) / m[0]
        if j > ave:
            count +=1
    r = count/m[0]*100
    print('{0:0.3f}%'.format(r))