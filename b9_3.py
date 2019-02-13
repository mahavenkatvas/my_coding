s=input()
l=[]

if '/' in s:
	l=s.split("/")
	print(int(l[0])//int(l[1]))
elif "%" in s:
	l=s.split("%")
	print(int(l[0])%int(l[1]))
