n,k=map(int,input().split())
s1=input()
l=[int(x) for x in input().split()]
l1=[int(x) for x in input().split()]
s=[]
for i in range(len(l1)):
	l.append(l1[i])
	x=max(l)
	s.append(x)
print(*s)
