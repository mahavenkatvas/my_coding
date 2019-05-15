n=input()
n=list(n)
l=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
l2=[]
l3=[]
c=0
for i in n:
  if i!=" ":
    l2.append(i)
for i in l2:
  if i in l and i not in l3:
    l3.append(i)
if len(l3)==26:
  print("yes")
else:
  print("no")
