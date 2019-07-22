n=int(input())
c=0
for i in range(n):
	x,t=map(int,input().split(" "))
	if x<t:
		c=c+1
print(c)
