n=int(input())
l=[str(x) for x in input().split(" ")]
x=sorted(l)
x="".join(x)
l="".join(l)
if x==l:
    print("yes")
else:
    print("no")
