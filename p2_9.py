def prime(n):
    i=2
    while i<n:
        if n%i==0:
            break
        i+=1
    if n==i:
        return 1
n=int(input())
if n%2!=0:
    print(n)

else:
    l=[2]
    for i in range(3,n//2):
       x=prime(i)
       if x==1:
           l.append(i)
    for i in range(len(l)):
        if n%l[i]==0:
            print(l[i],end=" ")
        
        
