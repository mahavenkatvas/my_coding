n=int(input())
l=[int(x) for x in input().split()]
s=[]
for i in range(len(l)):
    for j in range(i+1,len(l)):
         x=l[i]+l[j]
         for k in range(j+1,len(l)):
             if x==l[k]:
                s.append(l[k])
                print(l[i],l[j],l[k])
                break
