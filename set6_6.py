s=input()
if len(s)>0:
    if any(i.isalpha() for i in s) and any(i.isdigit() for i in s):
        print("Yes")
    else:
        print("No")
