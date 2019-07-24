n,k=map(int,input().split(" "))
flag=0
for i in range(n//2):
    if n==k**i:
        flag=1
        break
    elif k**i>n:
        break
    
if flag==1:
    print("yes")
else:
    print("no")
