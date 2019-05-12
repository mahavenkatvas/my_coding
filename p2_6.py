n,k=map(str,input().split(" "))
c=0
l=[]
l1=[]
if len(n)==len(k):
    for i in n:
       x= n.count(i)
       l.append(x)
    for i in k:
       y=k.count(i)
       l1.append(y)
    for i in range(len(l)):
       if l[i]==l1[i]:
          c=c+1
    if c==len(l):
       print("yes")
    else:
       print("no")
else:
  print("no")
