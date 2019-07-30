for _ in range(int(input())):
    n=int(input())
    l1=list(map(int,input().split()))
    l1.reverse()
    l2=[0]*n
    i=n-1
    for i in range(0,n):
        if i==0:
            l2[0]=1
        else:
            if l1[i]*l1[i-1]>0:
                l2[i]=1
            else:
                l2[i]=l2[i-1]+1
    l2.reverse()
    for i in l2:
        print(i,end=' ')
    print(end='\n')
