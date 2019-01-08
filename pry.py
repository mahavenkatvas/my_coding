n,k=map(int,input().split(" "))
n=n+1
l=[]
for n in range(n,k):
    i=2
    while i<n:
        if n%i==0:
            break
        i+=1
    if n==i:
        l.append(n)
  
for i in range(len(l)-1):
  print(l[i],end=" ")
print(l[-1])  
