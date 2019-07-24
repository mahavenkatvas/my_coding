n,m=map(str,input().split(" "))
m=int(m)
for i in range(m):
    x=n[-1]
    n=x+n[:-1]
print(n)

