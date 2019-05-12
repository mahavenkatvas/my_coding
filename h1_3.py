n=int(input())
l=[int(x) for x in input().split()]
x=[]
for i in range(len(l)):
     if l[i]==i:
        x.append(i)

for i in range(len(x)-1):
      print(x[i],end=" ")
print(x[-1])
