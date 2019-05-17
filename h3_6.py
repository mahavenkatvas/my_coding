n=input()
l=[int(x) for x in input().split()]
l.reverse()
for i in range(len(l)-1):
     print(l[i],end="->")
print(l[-1])
