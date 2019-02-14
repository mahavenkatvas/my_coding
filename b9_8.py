import math
n,m=map(int,input().split(" "))
x=(n*m//math.gcd(n,m))
print(x)
