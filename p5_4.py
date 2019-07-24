n,m=map(str,input().split(" "))
m=int(m)
for i in range(m):
    x=n[0]
    n=n[1:]+x
print(n)
