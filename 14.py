n,m=list(map(int,input().split()))
l=list(map(int,input().split()))
q=[]
while(m):
	k = list(map(int,input().split()))
	q.append(k)
	m-=1
for i in q:
	val=0
	for j in range(i[0]-1,i[1]):
		val=val^l[j]
	print(val)
