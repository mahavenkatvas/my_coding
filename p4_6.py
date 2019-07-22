n,k=map(int,input().split(" "))
c=0
while n!=0:
	x=n%10
	if k==x:
		c=c+1
	n=n//10
print(c)
