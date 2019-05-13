n=int(input())
l=[int(x) for x in input().split()]
k=[]
for i in range(len(l)):
     x=l.count(l[i])
     k.append(x)
h=k.count(1)
if h==0:
   print("unique")
else:
   for i in range(len(l)):
     if l.count(l[i])>1:
        print(l[i])
        break
      
