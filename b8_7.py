n=int(input())
l=[]
if n>0:
	for i in range(1,n+1):
		if n%i==0:
			l.append(i)
for i in range(len(l)-1):
 	print(l[i],end=" ")
print(l[-1])
