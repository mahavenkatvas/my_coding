s=input()
t=""
t1=""
for i in range(len(s)):
	if i%2==1:
		t=t+s[i]
	else:
		t1=t1+s[i]
print(t1,t)
