s=input()
l=list(s)
for i in range(len(l)):
	if l.count(l[i])>1:
	     break
if l.count(l[i])>1:
	print("No")
else:
	print("Yes")
