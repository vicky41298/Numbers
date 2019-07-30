n = int(input())
a,val = 3,3
while n > 0:
    if a == 0:
        val*=2
        a = val
    if n==1:
        print(a)
        break
    n -= 1
    a -= 1
