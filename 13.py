n,m = map(int,input().split())
l = list(map(int,input().split()))
for i in range(0,m) :
    a,b = map(int,input().split())
for i in range(0,m):
    print(min(l[a-1:b]))
