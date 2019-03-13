n=int(input())
sum=0
while n>0:
   x=n%10
   sum=sum+x**2
   n=n//10
print(sum)
