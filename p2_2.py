n,k=map(int,input().split(" "))
l=[int(x) for x in input().split()]
i=0
while i<k:
    l.insert(0,l[-1])
    l.pop()
    i=i+1
for i in range(len(l)-1):
    print(l[i],end=" ")
print(l[-1])
