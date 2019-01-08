n=int(input())
if n>60:
    r=n//60
    n=n-7*60
    print(r,n)
else:
    print(0,n)
