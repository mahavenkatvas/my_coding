from itertools import permutations
n=input()
x=permutations(n)
for i in list(x):
    print("".join(i))
