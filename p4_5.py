n=input()
n=list(n)
k=""
p=[]
for i in n:
    if i!=" ":
        x= n.count(i)
        p.append(x)
    else:
        p.append(2)
s=min(p)
for i in range(len(n)):
    if p[i]==s:
        k=k+" "+n[i]
print(k)
