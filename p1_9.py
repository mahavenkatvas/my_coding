#maha
def prime(n):
    i=2
    while i<=n-1:
        if n%i==0:
           break
        i+=1
    if n==i:
        return 1
