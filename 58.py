p = int(input())
s = []
d = p//2 + p
for i in range(1,p+1):
  if i%2==0:
    s.append(i)
for i in range(1,p+1):
  if i%2!=0:
    s.append(i)
for i in range(1,p+1):
  if i%2==0:
    s.append(i)
print(d)
print(*s
