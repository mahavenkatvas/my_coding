a,b,k=map(str,input().split())
k=int(k)
a=list(a)
b=list(b)
c=0
if len(a)==len(b):
  for i in range(len(a)):
    if a[i]!=b[i]:
      c=c+1
if c==k:
  print("yes")
else:
  print("no")
    
