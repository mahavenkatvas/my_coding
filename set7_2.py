s=input()
l=list(s)
c=0
for i in range(0,len(l)):
	if int(l[i])!=0 and int(l[i])!=1:
		c=c+1

if c>0:
	print("no")
else:
	print("yes")
