n,m=map(int,input().split(" "))
l=[int(x) for x in input().split()]
for i in range(len(l)):
    if m==l[i]:
       print("yes")
       break
else:
     print("no")
