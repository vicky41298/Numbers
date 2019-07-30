n=input()
m=n.count("@")
a=n.count(".")
for i in range(len(n)-2):
	if n[i]=="@":
		x=n[:i]
		b=i
	if n[i]==".":
		y=n[b+1:i]
if m==1 and a==1 and len(x)>=3 and len(y)<=5 and n[len(n)-4:]==".com":
	print("YES")
else:
	print("NO")
