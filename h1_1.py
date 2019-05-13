n=int(input())
l=[int(x) for x in input().split()]
k=[]
s=[]
for i in range(len(l)):
   x=l.count(l[i])
   k.append(x)
for i in range(len(k)):
    if k[i]>1 and l[i] not in s:
         s.append(l[i])
s.sort()
print(*s)
