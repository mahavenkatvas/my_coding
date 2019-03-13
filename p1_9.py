#maha
def prime(n):
    i=2
    while i<=n-1:
        if n%i==0:
           break
        i+=1
    if n==i:
        return 1
  
  
  
n,m=map(int,input().split(" "))
c=0
for i in range(n,m+1):
     x=prime(i)
     if x==1:
        c=c+1 
print(c)
