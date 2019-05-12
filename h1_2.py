n=int(input())
l=[int(x) for x in input().split()]
k=[]
for i in range(len(l)):
    x=max(l)
    k.append(x)
    l.remove(x)
for i in range(len(k)):
      print(k[i],end=""))
