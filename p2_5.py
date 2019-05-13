s=input()
s=list(s)
l=[]
for i in range(len(s)):
    x=s.count(s[i])
    l.append(x)
x=max(l)
p=l.index(x)
print(s[p])
