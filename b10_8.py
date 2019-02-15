n=int(input())
l=[int(x) for x in input().split()]
x=sorted(l)
for i in range(len(l)):
	if l[i]!=x[i]:
		print(l.index(l[i]))
		break
		
