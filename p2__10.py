s=input()
s=list(s)
l=[]
for i in range(len(s)):
    x=chr(ord(s[i])+3)
    l.append(x)
for i in range(len(l)):
    print(l[i],end="")
