n=input()
if n.isalnum():
	print(n)
	for i in n:
		if i.isnumeric():
			print(i,end="")
