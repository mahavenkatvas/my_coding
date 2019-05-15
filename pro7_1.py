n=input()
s=input()
l=["","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
l1=[]
l2=[]
l3=[]
ans=""
if len(n)==len(s):
  for i in n:
    j=0
    while j<len(l):
      if i==l[j]:
        l1.append(j)
      j+=1
  for i in s:
    j=0
    while j<len(l):
      if i==l[j]:
        l2.append(j)
      j+=1
  for i in range(len(l1)):
    x=l1[i]+l2[i]
    l3.append(x)
  for i in l3:
    if i>26:
      i=i-26
      ans=ans+l[i]
    else:
      ans=ans+l[i]
  print(ans)
