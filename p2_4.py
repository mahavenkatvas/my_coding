n=int(input())
s=input()
s=list(s)
r=["a","e","i","o","u","A","E","I","O","U"]
l=[]
for i in range(len(s)):
      if s[i] not in r:
          l.append(s[i])
for i in reversed(l):
    print(i,end="")
