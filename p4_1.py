s=input()
l=[]
k=[]
for i in s:
  if i=='(':
    l.append(i)
  elif i==')':
    k.append(i)
if len(k)==len(l):
  print("yes")
else:
  print("no")
