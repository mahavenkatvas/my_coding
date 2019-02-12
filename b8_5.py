s=input()
r=""
x=len(s)//2
if len(s)%2==0:
	for i in range(len(s)):
		print(s[:x-1]+"**"+s[x+1:])
else:
	for i in range(len(s)):
		print(s[:x]+"*"+s[x+1:])
		
