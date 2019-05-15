def dis(x1,y1,x2,y2):
  import math
  d=math.sqrt(((x2-x1)**2)+((y2-y1)**2))
  return d
a1,a2=map(int,input().split())
b1,b2=map(int,input().split())
c1,c2=map(int,input().split())
d1,d2=map(int,input().split())
w=dis(a1,b1,a2,b2)
x=dis(c1,c2,d1,d2)
y=dis(a1,a2,d1,d2)
z=dis(b1,b2,c1,c2)
print(w,x,y,z)
if w==x and x==y and y==z:
  print("yes")
else:
  print("no")
