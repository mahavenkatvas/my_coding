s=input()
l=[int(x) for x in input().split()]
s=[]
for i in range(len(l)):
    x=l.count(l[i])
    s.append(x)
for i in range(len(s)):
    if s[i]==1:
        print(s[i])
