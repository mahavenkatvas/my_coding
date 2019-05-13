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
if len(s)!=0:
    s.sort()
    print(*s)
else:
    print("unique")
