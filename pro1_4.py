n,k=map(str,input().split(" "))
l=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
x=0
for i in n:
	if i in l:
		x=x+(l.index(i)+1)
z=0
for i in k:
	if i in l:
		z=z+(l.index(i)+1)
print(abs(x-z))
		
		
