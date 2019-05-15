n,k=map(int,input().split())
l=[int(x) for x in input().split()]
c=0
for i in range(len(l)-1):
  for j in range(1,len(l)):
    if l[i]+l[j]==k:
      c+=1
if c>0:
  print("yes")
else:
  print("no")

