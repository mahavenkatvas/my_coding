n=int(input())
if n>=2:
    i=2
    while i<n:
        if n%i==0:
            break
        else:
            i+=1
if n==i:
    print("yes")
else:
    print("no")
