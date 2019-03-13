#maha
s=input()
r=s.split(" ")
l=[]
for i in range(len(r)):
   x=r[i][0].upper()+r[i][1:]
   l.append(x)
l=' '.join(l)
print(l)
