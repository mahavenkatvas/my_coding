n=input()
l=list(n)
x=sorted(l)
for i in range(len(x)-1):
	print(x[i],end="")
print(x[-1])
