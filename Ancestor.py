def traverseback(parent,x):
    if(parent==-1):
       x.append(-1)
       return x

    x.append(parent)
    return traverseback (l[parent],x)
l=List(map(int, input().split()))
a,b=map(int,input().split())
parentsA, parentsB=[a],[b]
parentsA, parentsB=traverseback(l[a], parentsA), traverseback (1[b], parentsB)
print(l, parentsA, parentsB)
for i in range(1, max(len(parentsA), len(parentsB))):
    if(parentsA[-i]!=parentsB[-i]):


        print(parentsA[-i+1])
        exit()



if(len (parentsA) <len(parentsB)):
        print(parentsA[0])



else:


      print(parentsB[0])
