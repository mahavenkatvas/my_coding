n=int(input())
l=[]
while n>0:
	x=n%10
	if x%2==1:
		l.append(x)
	n=n//10
l=l[::-1]
for i in range(len(l)-1):
	print(l[i],end=" ")
print(l[-1])
