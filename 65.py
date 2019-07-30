n,k= map(int,input().split())
l = list(map(int,input().split()))
price = int(input())
val = (sum(l)-l[k])//2
if price == val:
    print("Bon Appetit")
else:
    print(price-val)
