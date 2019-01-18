#maha
n,k=map(int,input().split(" "))
sum=0
l=[a for a in range(1,n+1)]
for i in range(k):
  sum=sum+l[i]
print(sum)  
  
