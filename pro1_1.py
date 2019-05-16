n=int(input())
l=[]
s=[]
b=""
d=[]
for i in range(n):
    p=input()
    x=len(p)
    s.append(x)
    l.append(p)
k=min(s)
for i in range(len(l)-1):
    j=0
    while j<k:
      if l[0][j]==l[i+1][j]:
          b=b+l[i][j]
          j+=1
          
      else:
          k=len(b)
          break
    d.append(b)
print(d[0])
