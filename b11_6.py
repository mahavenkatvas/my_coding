#maha
n,k=map(int,input().split(" "))
l=[int(x) for x in input().split()]
j=0
for i in range(len(l)):
     if j<k:
       if l[i]%2==1:
          x=l[i]
          j+=1
print(x)
