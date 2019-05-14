n=input()
n=list(n)
l=[]
for i in range(len(n)):
  if i%3==0:
    l.append(n[i])
for i in range(len(l)):
  print(l[i],end="")
