#1.PROGRAM CODE :
n=int(input())
a=list(map(int,input().split()))
for j in range(n+1):
	for i in range(n-1):
    	if(a[i]>a[i+1]):
        	t=a[i]
        	a[i]=a[i+1]
        	a[i+1]=t
print(a)

"""OUTPUT:
5
6 4 3 2 5
[2, 3, 4, 5, 6]"""

#2.PROGRAM CODE :
n=int(input())
a=list(map(int,input().split()))
for j in range(n+1):
	for i in range(n-1):
    	if(a[i]>a[i+1]):
        	t=a[i]
        	a[i]=a[i+1]
        	a[i+1]=t
print(a)
"""OUTPUT:
5
6 4 3 2 5
[2, 3, 4, 5, 6]"""

#3.PROGRAM CODE :
n=int(input())
a=list(map(int,input().split()))
for j in range(n+1):
	for i in range(n-1):
    	if(a[i]>a[i+1]):
        	t=a[i]
        	a[i]=a[i+1]
        	a[i+1]=t
print(a)

"""OUTPUT:
5
6 4 3 2 5
[2, 3, 4, 5, 6]"""
