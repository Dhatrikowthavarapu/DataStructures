#1.PROGRAM  CODE  :

l=[]
found=0
n=int(input("enter the total number of elements "))
print("enter 8 elements")
l=list(map(int,input().split(",")))
for i in range(n-1):
	for j in range((n-1)-i):
    	if(l[j]>l[j+1]):
        	t=l[j]
        	l[j]=l[j+1]
        	l[j+1]=t
key=int(input("enter element to search "))
low,high=1,n
while(low<=high):
	mid=(high+low)//2
	if(key<l[mid]):
    	high=mid-1
	elif(key>l[mid]):
    	low=mid+1
	elif(key==l[mid]):
    	print(key," is present at the location ",mid)
    	found=1
    	break

"""OUTPUT :
enter the total number of elements 8
enter 8 elements
44,16,18,164,47,10,0,-68
enter element to search 10
10  is present at the location  2"""

#2.PROGRAM  CODE  :
l=[]
found=0
n=int(input("enter the total number of jails in Humayun's Place :\n"))
for i in range(n):
	l.append(int(input("enter the jail number {}\n".format(i+1))))
key=int(input("enter the clue given by Humayun :\n"))
low,high=1,n
while(low<=high):
	mid=(high+low)//2
	if(key<l[mid]):
    	high=mid-1
	elif(key>l[mid]):
    	low=mid+1
	elif(key==l[mid]):
    	print(key)
    	found=1
    	print("Hurray!The King rescued the Queen")
    	break
if(found==0):
	print("The King has been fooled by the Humayun")

  """OUTPUT-1  :
enter the total number of jails in Humayun's Place :
5
enter the jail number 1
6
enter the jail number 2
89
enter the jail number 3
91
enter the jail number 4
105
enter the jail number 5
200
enter the clue given by Humayun :
105
105
Hurray!The King rescued the Queen
OUTPUT-2   :
enter the total number of jails in Humayun's Place :
6
enter the jail number 1
56
enter the jail number 2
68
enter the jail number 3
156
enter the jail number 4
196
enter the jail number 5
204
enter the jail number 6
895
enter the clue given by Humayun :
4
The King has been fooled by the Humayun"""


#3.PROGRAM CODE  :
def primicity(a):
	count=0
	numberofprime=0
	for i in a:
    	if(i%j==0):
        	break
    	else:
        	numberofprime+=1
        	if(numberofprime<=k):
            	count+=1
            	return count
n=int(input("enter number of elements "))
l=list(map(int,input("enter elements:").split(",")))
k=int(input("enter k :"))
a=[]
for i in range(len(l)+1):
	for j in range(i+1,len(l)+1):
    	sub=l[i:j]
    	a.append(sub)
sum=0
for i in count:
	if(primicity(i)<=k):
    	ans+=1
    	print(i)
	print(ans)
OUTPUT   :
enter number of elements 8
enter elements:2,3,4,5
enter k :2
[2]
[2,3]
[3]
[2,3,4]
[3,4]
[4]
[4,5]
[5]
[]
