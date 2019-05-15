n=int(input("k = "))
l1=[]
for i in range(n):
  l=[int(x) for x in input().split()]
  for i in l:
    l1.append(i)
x=sorted(l1)
print(*x)

