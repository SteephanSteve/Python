#!usr/bin/python

n=int(raw_input("Enter the no. of elements :"))
a=[]
b=[]
print "Enter the elements :"
for i in xrange(n):
    x=int(input())
    a.append(x)
for i in xrange(n):
    if (i%2==0 and a[i]%2!=0) or (i%2!=0 and a[i]%2==0):
        b.append(a[i])
if b:
    print b
    
        
