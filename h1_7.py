n=int(input())
l=[int(x) for x in input().split()]
x=[]
for i in range(len(l)):
    if i%2==0:
        if l[i]%2!=0:
            x.append(l[i])
    else:
        if l[i]%2==0:
            x.append(l[i])
print(*x)
