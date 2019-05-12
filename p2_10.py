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
    s=l.count(1)
    t=l1.count(1)
    if s==1 and t==1:
       print("yes")
    else:
       print("no")
else:
  print("no")
