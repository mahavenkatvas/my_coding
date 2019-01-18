#maha
n,k=map(int,input().split(" "))
n=n+1
l=[]
while n<k:
  if n%2==1:
    l.append(n)
  n+=1 
for i in range(len(l)-1):
  print(l[i],end=" ")
print(l[-1])

  
