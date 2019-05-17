#maha
x,y=map(str,input().split())
p=abs(len(x)-len(y))
c=0
if len(x)>len(y):
    if y in x:
        c=p
    else:
        c=0
else:
    y=y[:len(x)]
    for i in range(len(x)):
       if x[i]!=y[i]:
           c=c+1
    c=c+p
print(c)
