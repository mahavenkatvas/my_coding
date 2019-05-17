x,y=map(str,input().split())
c=0
if len(x)>len(y):
    l=x[:len(y)]
    for i in range(len(l)):
        if l[i] == y[i]:
            c=c+1
    dif=len(x)-c        
else:
    l=y[:len(x)]
    for i in range(len(l)):
        if l[i] == x[i]:
            c=c+1
    dif=len(y)-c      
print(dif)
