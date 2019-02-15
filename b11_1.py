s,n=map(str,input().split(" "))
n=int(n)
x=s[::-1]
l=[]
for i in range(n):
	l.append(x[i])
l.reverse()
for i in range(len(l)):
	print(l[i],end="")
	
