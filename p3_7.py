#maha
s=input()
x=""
for i in s:
	if i.isupper():
		x=x+i.lower()
	else:
		x=x+i.upper()
print(x)
