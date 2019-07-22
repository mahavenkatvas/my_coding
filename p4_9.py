n=int(input())
if n>2:
	x=n//2
else:
	x=n
flag=0
for i in range(x):
	if 2**i==n:
		flag=1
		break
if flag==1:
	print("yes")
else:
	print("no")
	
		
