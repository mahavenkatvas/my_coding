s,k=map(str,input().split(" "))
k=int(k)
j=0
for i in s:
    if j<k:
        print(i,end="")
        j=j+1
