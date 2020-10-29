"""
x1,y1=input().split()
x=int(x1)
y=float(y1)
print('%.2f' %((y-x-0.50)) )


try:
    #code that may throw an error
    x1,y1=input().strip().split()
    x=int(x1)
    y=float(y1)
    if x%5==0 and x+0.5<y:
    	print('%.2f' %((y-x-0.50)) )
    else:
    	print('%.2f'%y)
except:
    pass


x,y = map(float, input().split())
if (x%5)==0 and (x+0.5<=y):
    print(y-(x+0.5))
else:print(y)

n=int(input())
for i in range(n):
	x,y=map(int,input().split())
	a=x%y
	print(a)




def factn(num):
	fact=1
	for i in range(1,num+1):
		fact*=i
	return fact
n=int(input())
for i in range(n):
	k=int(input())
	a=factn(k)
	print(a)

n=int(input())
l=[]
for i in range(n):
	k=int(input())
	l.append(k)
v=sorted(l)
for i in v:
	print(i,end="\n")

n=int(input())
for i in range(n):
	k=input()
	c=0
	for i in k:
		if i=='4':
                        c+=1
	print(c)

n=int(input())
for i in range(n):
	k=input()
	print(k[::-1])
"""
n=int(input())
p1,p2=[],[]

for i in range(n):
	
	a,b=map(int,input().split())
	if a>b:
		p1.append(a-b)
	else:
		p2.append(b-a)
if max(p1)>max(p2):
	print("1",max(p1))
else:
	print("2",max(p2))
