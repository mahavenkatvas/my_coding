#maha
from itertools import combinations
n,k=map(int,input().split())
s=len(str(n))
l=list(combinations(str(n),s-k))
print(l)
l=sorted(l)
print("".join(l[0]))
