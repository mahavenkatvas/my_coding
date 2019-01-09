n=int(input())
i=0
j=1
l=[]
for i in range(n):
    k=i+j
    i=j
    j=k
    l.append(k)
for i in range(len(l)-1):
    print(l[i],end=" ")
print(l[-1])    
