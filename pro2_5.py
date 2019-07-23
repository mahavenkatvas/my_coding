n=int(input())
l=[int(x) for x in input().split(" ")]
l.sort()
x=l[::-1]
for i in range(len(x)):
	print(x[i])
