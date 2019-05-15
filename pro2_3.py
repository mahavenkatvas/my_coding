n,k=map(int,input().split())
l=[int(x) for x in input().split()]
l1=[]
for i in range(k):
  x=[int(x) for x in input().split()]
  l1.append(x)
for i in range(len(l1)):
  k=l1[i][0]
  j=l1[i][1]
  x=l[k-1:j]
  print(min(x))
