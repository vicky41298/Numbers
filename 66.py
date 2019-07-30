a, b, c, d = map(int, input().split())
count = 0
a2 = b-c
if (a2 >= 0):
    m = (a-c)*2
    for i in range(d):
        if (i == d-1):
            m/=2
        if (a2 < m):
            a2 = b
            count += 1
        a2-=m
        if (a2 < 0):
            count = -1
            break
        m = 2*a -m
    print(count)
else:
    print(-1)
