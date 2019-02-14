n=input()
if n.isalnum():
	for i in n:
		if i.isnumeric():
			print(i,end="")
