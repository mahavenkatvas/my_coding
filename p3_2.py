n,k=map(int,input().split())
if n>k:
	x=n
else:
	x=k
for i in range(x,1,-1):
	if n%i==0 and k%i==0:
		print(i)
		break
