n=int(input())
l=[]
while n>0:
   x=x%10
   n=n//10
   l.append(x)
for i in range(len(l)-1):
   print(l.pop(),end=" ")
print(l[0])
   
