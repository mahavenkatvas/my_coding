n=int(input())
s="kabali"
s=list(s)
t=0
for i in range(n):
    x=input()
    if len(s)==len(x):
        x=list(x)
        c=0
        for i in range(len(s)):
            if x[i] in s:
                c=c+1
        if c==len(s):
            t=t+1
print(t)
