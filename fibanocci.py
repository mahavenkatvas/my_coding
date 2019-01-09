n=int(input())
i=0
j=1
l=[1]
for x in range(n-1):
    k=i+j
    i=j
    j=k
    l.append(k)
for i in range(len(l)-1):
    print(l[i],end=" ")
print(l[-1])    
