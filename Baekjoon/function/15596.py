def solve(a):
    result = 0
    for i in range(len(str(a))):
        result += int(str(a)[i])
    result += a
    return result

list1=[]
for i in range(1, 10001):
    list1.append(i)

n=0
l=[]
while True:
    n=n+1
    if n > 10000:
        break
    l.append(solve(n))

self_num_set=set(list1)-set(l)

self_num_list=list(self_num_set)
self_num_list.sort()

for i in self_num_list:
    print(i)




