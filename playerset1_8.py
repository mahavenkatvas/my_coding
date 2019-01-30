s=input()
s=s.split(" ")
print(s)
for i in s:
    print(i[0].upper()+i[1:].lower(),end=" ")
