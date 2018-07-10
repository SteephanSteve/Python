#!usr/bin/python

n=int(raw_input("Enter the no. of elements :"))
a=[]
b=[]
print "Enter the elements :"
for i in xrange(n):
    x=int(input())
    a.append(x)
for i in xrange(n):
    for j in range(i+1,n):
        if a[i]==a[j]:
            a[i]=a[j]=0
for i in xrange(n):
    if not a[i]==0:
        print a[i]
