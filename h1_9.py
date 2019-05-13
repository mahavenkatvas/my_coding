n=int(input())
l=[int(x) for x in input().split()]
for i in range(len(l)):
    if l[i]<0:
        for j in range(len(l)):
            if abs(l[i])==l[j]:
                print(l[i],l[j])
                break
if l.count(0)%2==0:
    print("0 0")
