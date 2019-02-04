n=int(input())
c=0
if n>=2:
  i=2
  while i<n:
    if n%i==0:
    	c+=1
    i+=1
if c>0:
  print("yes")
else:
  print("no")
