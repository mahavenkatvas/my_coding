n=int(input())
l=[]
for i in range(2,n+1,2):
	if n%i==0:
		l.append(i)
print(*l)
