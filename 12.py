n,m=list(map(int,input().split()))
l=list(map(int,input().split()))
for i in range(m):
    a,b=list(map(int,input().split()))
    print(sum(l[a-1:b]))
