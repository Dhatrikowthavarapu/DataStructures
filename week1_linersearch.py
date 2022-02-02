#1.Program code:
found=0
print("enter the number of elements : ")
n=int(input())
print("enter the elements : ")
l=list(map(int,input().split()))
key=int(input("enter the number to be checked : "))
for i in range(n):
	if l[i]==key:
    	found=1
    	print(str(key)+" is present in the location of "+str(i))
    	break
if(found==0):
	print("element not found")

"""output:
enter the number of elements :
8
enter the elements :
44 16 18 164 47 10 0 -68
enter the number to be checked : 10
10 is present in the location of 5"""


#2.PROGRAM  CODE :
found=0
print("enter the number of elements : ")
n=int(input())
print("enter the elements : ")
l=list(map(int,input().split()))
key=int(input("enter the number to be checked : "))
for i in range(n):
	if l[i]==key:
    	found+=1
    	print(str(key)+" is present in the location of "+str(i))
if(found==0):
	print("element not found")


"""output:
enter the number of elements :
6
enter the elements :
44 16 18 16 47 16
enter the number to be checked : 16
16 is present in the location of 1
16 is present in the location of 3
16 is present in the location of 5"""


#3.PROGRAM  CODE :

found=0
print("enter the number of elements : ")
n=int(input())
print("enter the elements : ")
l=list(map(int,input().split()))
key=int(input("enter the number to be checked : "))
for i in range(n):
	if l[i]==key:
    	found+=1
    	print(str(key)+" is present in the location of "+str(i))
if(found==0):
	print("element not found")

"""OUTPUT :
enter the number of elements :
6
enter the elements :
44 16 18 16 47 16
enter the number to be checked : 16
16 is present in the location of 1
16 is present in the location of 3
16 is present in the location of 5"""
