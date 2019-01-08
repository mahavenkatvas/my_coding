#mahalakshmi
n=int(input())
x=n
ams=0
while n>0:
    r=n%10
    ams=ams+r**3
    n=n//10
if x==ams:
    print("yes")
else:
    print("no")
