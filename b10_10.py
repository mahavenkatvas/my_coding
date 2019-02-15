n=int(input())
p=1
while n>0:
	x=n%10
	p=p*x
	n=n//10
print(p)
