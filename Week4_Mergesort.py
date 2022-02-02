def merge(a,p,r):
    if p<r:
        q=(p+r)//2
        merge(a,p,q)
        merge(a,q+1,r)
        merge_1(a,p,q,r)
    return a
def merge_1(a,p,q,r):
    n1=q-p+1
    n2=r-q
    l,m=[],[]
    for i in range(n1):
        l.append(a[i+p])
    for j in range(n2):
        m.append(a[j+q+1])
    l.append(1000000000000000)
    m.append(1000000000000000)
    i=j=0
    for k in range(p,r+1):
        if l[i]<m[j]:
            a[k]=l[i]
            i+=1
        else:
            a[k]=m[j]
            j+=1
    return a
n=int(input())
a=[]
for i in range(n):
    b=int(input("enter number to list:"))
    a.append(b)
print(a)
p=0
r=len(a)-1
print(merge(a,p,r))
